# -*- coding: utf-8 -*-

__version__ = "0.20.0"

import importlib

from .mendeleev import (  # noqa: F401
    element,
    isotope,
    get_all_elements,
    get_attribute_for_all_elements,
)


_symbols = [
    "H",
    "He",
    "Li",
    "Be",
    "B",
    "C",
    "N",
    "O",
    "F",
    "Ne",
    "Na",
    "Mg",
    "Al",
    "Si",
    "P",
    "S",
    "Cl",
    "Ar",
    "K",
    "Ca",
    "Sc",
    "Ti",
    "V",
    "Cr",
    "Mn",
    "Fe",
    "Co",
    "Ni",
    "Cu",
    "Zn",
    "Ga",
    "Ge",
    "As",
    "Se",
    "Br",
    "Kr",
    "Rb",
    "Sr",
    "Y",
    "Zr",
    "Nb",
    "Mo",
    "Tc",
    "Ru",
    "Rh",
    "Pd",
    "Ag",
    "Cd",
    "In",
    "Sn",
    "Sb",
    "Te",
    "I",
    "Xe",
    "Cs",
    "Ba",
    "La",
    "Ce",
    "Pr",
    "Nd",
    "Pm",
    "Sm",
    "Eu",
    "Gd",
    "Tb",
    "Dy",
    "Ho",
    "Er",
    "Tm",
    "Yb",
    "Lu",
    "Hf",
    "Ta",
    "W",
    "Re",
    "Os",
    "Ir",
    "Pt",
    "Au",
    "Hg",
    "Tl",
    "Pb",
    "Bi",
    "Po",
    "At",
    "Rn",
    "Fr",
    "Ra",
    "Ac",
    "Th",
    "Pa",
    "U",
    "Np",
    "Pu",
    "Am",
    "Cm",
    "Bk",
    "Cf",
    "Es",
    "Fm",
    "Md",
    "No",
    "Lr",
    "Rf",
    "Db",
    "Sg",
    "Bh",
    "Hs",
    "Mt",
    "Ds",
    "Rg",
    "Cn",
    "Nh",
    "Fl",
    "Mc",
    "Lv",
    "Ts",
    "Og",
]


def __getattr__(name):
    """
    Dynamically creates an element object and stores it in the module's namespace.

    Args:
        name (str): The symbol of the element to be created.

    Returns:
        Element: The element object corresponding to the provided symbol.

    Raises:
        ImportError: If the element symbol is not found in _symbols.

    Examples:
        Usage:
        >>> from mendeleev import C
        >>> print(C.atomic_number)
        6
    """
    if name in _symbols:
        element_obj = element(name)  # noqa: F405
        globals()[name] = element_obj
        return element_obj

    # attempt to import the module if it's not an element symbol
    try:
        module = importlib.import_module(name)
        globals()[name] = module
        return module
    except ModuleNotFoundError as e:
        raise AttributeError(f"module 'mendeleev' has no attribute '{name}'") from e
