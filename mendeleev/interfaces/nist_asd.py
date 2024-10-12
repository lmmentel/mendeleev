"""Interface to the NIST Atomic Spectra Database (ASD)"""

import io
from enum import Enum

import pandas as pd
import requests
from pydantic import BaseModel


class Units(Enum):
    cm_1 = 0
    eV = 1
    Rydberg = 2
    Hartree = 3
    GHz = 4


class Format(Enum):
    HTML = 0
    ASCII = 1
    CSV = 2
    TAB_DELIMITED = 3


class Query(BaseModel):
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
    base_url: str = "https://physics.nist.gov/cgi-bin/ASD/ie.pl"

    def request(self):
        params = {k: v for k, v in self.model_dump().items() if k not in {"base_url"}}

        return f"{self.base_url}?" + "&".join([f"{k}={v}" for k, v in params.items()])

    def fetch_data(self):
        response = requests.get(self.request())
        response.raise_for_status()

        # find the Notes section if exists
        try:
            index = response.text.index("Notes")
        except ValueError:
            index = len(response.text)
        csv_data = response.text[:index]
        # csv_notes = response.text[index:]
        csv_file = io.StringIO(csv_data)
        return pd.read_csv(csv_file)


def clean(df):
    "Clean the data frame from NIST ASD"
    df = df.dropna(axis="columns")
    df = df.apply(lambda x: x.str.strip("="))
    df = df.apply(lambda x: x.str.strip('"'))
    df["At. num"] = pd.to_numeric(df["At. num"])
    df["Ionization Energy (eV)"] = pd.to_numeric(df["Ionization Energy (eV)"])
    df["Uncertainty (eV)"] = pd.to_numeric(df["Uncertainty (eV)"])
    return df
