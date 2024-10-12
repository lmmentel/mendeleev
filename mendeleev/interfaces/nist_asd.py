"""Interface to the NIST Atomic Spectra Database (ASD)"""

from pydantic import BaseModel
from enum import Enum


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
    units: int = Units.eV
    format: int = Format.CSV
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
        return f"{self.base_url}?" + "&".join(
            [f"{k}={v}" for k, v in self.dict().items()]
        )
