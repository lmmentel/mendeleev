"""Interface to the NIST Atomic Spectra Database (ASD)"""

import asyncio
import io
import time
from enum import Enum
from pathlib import Path

import httpx
import pandas as pd
from pydantic import BaseModel

from mendeleev.db import get_session
from mendeleev.mendeleev import get_attribute_for_all_elements
from mendeleev.models import IonizationEnergy


class Units(Enum):
    """Units for the ionization energy with their corresponding values"""

    cm_1 = 0
    eV = 1
    Rydberg = 2
    Hartree = 3
    GHz = 4


class Format(Enum):
    """Format for the output data with their corresponding values"""

    HTML = 0
    ASCII = 1
    CSV = 2
    TAB_DELIMITED = 3


class NISTIEQuery(BaseModel):
    spectra: str
    units: int = Units.eV.value
    format: int = Format.CSV.value
    order: int = 0
    at_num_out: str = "on"
    sp_name_out: str = "on"
    ion_charge_out: str = "on"
    el_name_out: str = "on"
    seq_out: str = "on"
    shells_out: str = "on"
    conf_out: str = "on"
    level_out: str = "on"
    ion_conf_out: str = "on"
    e_out: int = 0
    unc_out: str = "on"
    biblio: str = "on"
    submit: str = "Retrieve+Data"

    def get_full_url(self):
        """Full for the query"""
        base_url: str = "https://physics.nist.gov/cgi-bin/ASD/ie.pl"
        return f"{base_url}?" + "&".join(
            [f"{k}={v}" for k, v in self.model_dump().items()]
        )


async def parse_to_dataframe(url: str, client, semaphore) -> tuple[pd.DataFrame, str]:
    """Parse the data from the NIST ASD to a pandas DataFrame"""
    text = await fetch_url_data(url, client, semaphore)

    if "Invalid query." in text:
        return None, None

    try:
        index = text.index("Notes")
    except ValueError:
        index = len(text)
    csv_data = text[:index]
    csv_notes = text[index:]
    csv_file = io.StringIO(csv_data)
    return pd.read_csv(csv_file), csv_notes


async def fetch_url_data(url: str, client, semaphore):
    async with semaphore:
        response = await client.get(url)
        response.raise_for_status()
        return response.text


async def write_csv(element: str, url: str, path: Path, client, semaphore):
    """Write the data to a csv file, and the notes to a txt file"""
    df, notes = await parse_to_dataframe(url, client, semaphore)
    if df is not None:
        df.to_csv(path.joinpath(f"{element}.csv"), index=False)
    if notes:
        with open(path.joinpath(f"{element}.txt"), "w") as f:
            f.write(notes)


async def bulk_fetch_and_save(elements: list[str], dest: Path):
    """Fetch ionization energy data from NIST ASD and save it to a csv file."""
    semaphore = asyncio.Semaphore(20)
    async with httpx.AsyncClient() as client:
        tasks = []
        for element in elements:
            print(f"Fetching data for {element}")
            url = NISTIEQuery(spectra=element).get_full_url()
            tasks.append(write_csv(element, url, dest, client, semaphore))
        await asyncio.gather(*tasks)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the data frame from NIST ASD

    For Hydrogen the extra column "Ionised Level" was added since it's missing in the original data
    """

    columns = [
        "atomic_number",
        "species_name",
        "ion_charge",
        "element_name",
        "isoelectonic_sequence",
        "ground_shells",
        "ground_configuration",
        "ground_level",
        "ionized_level",
        "prefix",
        "ionization_energy",
        "suffix",
        "uncertainty",
        "references",
    ]

    df = df.dropna(axis="columns")
    df = df.iloc[:, :15]
    df.columns = columns
    df = df.apply(lambda x: x.str.strip("="))
    df = df.apply(lambda x: x.str.strip('"'))
    df["atomic_number"] = pd.to_numeric(df["atomic_number"])
    df["ionization_energy"] = pd.to_numeric(df["ionization_energy"])
    df["uncertainty"] = pd.to_numeric(df["uncertainty"])
    return df


def download_ie_data(path: Path):
    """Download ionization energy data from NIST ASD and save it to a csv file per element."""
    elements = get_attribute_for_all_elements("symbol")

    start_time = time.time()
    asyncio.run(bulk_fetch_and_save(elements=elements, dest=path))
    print(f"--- {time.time() - start_time} seconds ---")


def merge_ie_data(path: Path) -> pd.DataFrame:
    "Merge individual csv files into a single DataFrame"
    dfs = []
    for file in path.glob("*.csv"):
        df = pd.read_csv(file)
        dfs.append(df)

    df = pd.concat(dfs, axis=0)
    return df


def prepare_ie_table(ie: pd.DataFrame) -> pd.DataFrame:
    """Prepare the ionization energy table for storing in the database."""
    ie = ie.sort_values(by=["atomic_number", "ion_charge"])
    # create new flag based on souce from: https://physics.nist.gov/PhysRefData/ASD/Html/iehelp.html#IE_OUTPUT
    ie.loc[:, "is_semi_empirical"] = (ie.prefix == "[") & (ie.suffix == "]")
    ie.loc[:, "is_theoretical"] = (ie.prefix == "(") & (ie.suffix == ")")
    # drop the columns that are not needed
    ie = ie.drop(columns=["prefix", "suffix", "element_name"])
    # drop rows without the ioniztion energy
    ie = ie.dropna(axis=0, subset=["ionization_energy"])
    return ie


def process_ie_files(source: Path, destination: Path):
    for file in source.glob("*.csv"):
        print(f"Processing: {file}")
        df = pd.read_csv(file)
        try:
            df = clean(df)
        except Exception as e:
            print(f"ERROR: {e}")
            continue
        df.to_csv(destination.joinpath(file.name), index=False)


def udate_database():
    """Update the mendeleev database with the ionization energy data."""
    session = get_session(read_only=False)

    objects = [
        IonizationEnergy(
            atomic_number=row["atomic_number"],
            ground_configuration=row["ground_configuration"],
            ground_level=row["ground_level"],
            ground_shells=row["ground_shells"],
            ion_charge=row["ion_charge"],
            ionization_energy=row["ionization_energy"],
            ionized_level=row["ionized_level"],
            is_semi_empirical=row["is_semi_empirical"],
            is_theoretical=row["is_theoretical"],
            isoelectonic_sequence=row["isoelectonic_sequence"],
            references=row["references"],
            species_name=row["species_name"],
            uncertainty=row["uncertainty"],
        )
        for _, row in ie.iterrows()
    ]
    session.add_all(objects)
    session.commit()
    session.close()


if __name__ == "__main__":
    DOWNLOAD = False
    PROCESS = True

    if DOWNLOAD:
        raw = Path("data/ie")
        if not raw.exists():
            raw.mkdir(parents=True)
        download_ie_data(raw)

    if PROCESS:
        processed = Path("data/ie/processed")
        if not processed.exists():
            processed.mkdir(parents=True)
        process_ie_files(source=raw, destination=processed)

        # get the data readt for the database
        ie = merge_ie_data(processed)
        ie = prepare_ie_table(ie)
        ie.to_parquet(processed.joinpath("ionization_energies.parquet"), index=False)
