"""Interface to the NIST Atomic Spectra Database (ASD)"""

import asyncio
import io
import time
from enum import Enum
from pathlib import Path

import httpx
import pandas as pd
from pydantic import BaseModel

from mendeleev.mendeleev import get_attribute_for_all_elements


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


def clean(df):
    "Clean the data frame from NIST ASD"

    columns = [
        "atomic_number",
        "species_name",
        "ion_charge",
        "element_name",
        "Isoel. Seq.",
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

    df.columns = columns
    df = df.dropna(axis="columns")
    df = df.apply(lambda x: x.str.strip("="))
    df = df.apply(lambda x: x.str.strip('"'))
    df["atomic_number"] = pd.to_numeric(df["atomic_number"])
    # df["Ionization Energy (eV)"] = pd.to_numeric(df["Ionization Energy (eV)"])
    # df["Uncertainty (eV)"] = pd.to_numeric(df["Uncertainty (eV)"])
    return df


def download_ie_data():
    path = Path("data/ie")
    if not path.exists():
        path.mkdir(parents=True)
    elements = get_attribute_for_all_elements("symbol")[:10]

    start_time = time.time()
    asyncio.run(bulk_fetch_and_save(elements=elements, dest=path))
    print(f"--- {time.time() - start_time} seconds ---")


if __name__ == "__main__":
    download_ie_data()
