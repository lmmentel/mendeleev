"""Entry point for the Mendeleev package for instantiating elements and isotopes."""

from typing import List, Union

import sqlalchemy
from sqlalchemy.orm import Session

from .db import get_session, get_engine
from .models import Element, Isotope


__all__ = [
    "get_all_elements",
    "get_attribute_for_all_elements",
    "element",
    "isotope",
]


def element(ids: Union[int, str]) -> Element:
    """
    Based on the type of the `ids` identifier return either an
    :py:class:`Element <mendeleev.models.Element>` object from the
    database, or a list of :py:class:`Element <mendeleev.models.Element>`
    objects if the `ids` is a list or a tuple of identifiers. Valid
    identifiers for an element are: *name*, *symbol*, and
    *atomic number*.

    Args:
        ids (str): element identifier

    Raises:
        ValueError: when the identifier is not a list/tuple, int or str

    Example:
        The element can be identified by symbol

        >>> from mendeleev import element
        >>> si = element('Si')
        >>> si.atomic_number
        14

        by the atomic number

        >>> al = element(13)
        >>> al.name
        'Aluminum'

        or by the name

        >>> o = element('Oxygen')
        >>> o.symbol
        'O'

        Mutiple elements can be instantiated simultaneously through as
        combination of identifiers

        >>> c, h, o = element(['C', 'Hydrogen', 8])
        >>> print(c.name, h.name, o.name)
        Carbon Hydrogen Oxygen

    """
    if isinstance(ids, (list, tuple)):
        return [_get_element(i) for i in ids]
    elif isinstance(ids, (str, int)):
        return _get_element(ids)
    else:
        raise ValueError(
            "Expected a <list>, <tuple>, <str> or <int>, got: {0:s}".format(type(ids))
        )


def _get_element(ids) -> Union[Element, List[Element]]:
    """
    Return an element from the database based on the `ids` identifier passed.
    Valid identifiers for an element are: *name*, *symbol*, *atomic number*.
    """

    session = get_session()

    try:
        if isinstance(ids, str):
            if len(ids) <= 3 and ids.lower() != "tin":
                return session.query(Element).filter(Element.symbol == str(ids)).one()
            else:
                return session.query(Element).filter(Element.name == str(ids)).one()
        elif isinstance(ids, int):
            return session.query(Element).filter(Element.atomic_number == ids).one()
        raise ValueError("Expecting a <str> or <int>, got: {0:s}".format(type(ids)))
    except sqlalchemy.exc.NoResultFound:
        raise ValueError(f"Element not found: {ids}")


def get_all_elements() -> List[Element]:
    "Get all elements as a list"

    session = get_session()
    elements = session.query(Element).all()
    session.close()
    return elements


def isotope(symbol_or_atn: Union[str, int], mass_number: int) -> Isotope:
    """
    Get an Isotope based on the element symbol and mass number or atomic number
    and mass number.

    Args:
        symbol_or_atn (str or int): either element symbol or atomic number
        mass_number (int): mass number of the isotope

    Returns:
        isotope (Isotope): isotope instance
    """
    session = get_session()
    if isinstance(symbol_or_atn, int):
        return (
            session.query(Isotope)
            .filter_by(atomic_number=symbol_or_atn, mass_number=mass_number)
            .one()
        )
    elif isinstance(symbol_or_atn, str):
        return (
            session.query(Isotope)
            .join(Element)
            .filter(Element.symbol == symbol_or_atn, Isotope.mass_number == mass_number)
            .one()
        )
    else:
        raise ValueError(
            "Expecting a <str> or <int>, got: {0:s}".format(type(symbol_or_atn))
        )


def ids_to_attr(ids, attr: str = "atomic_number"):
    """
    Convert the element ids: atomic numbers, symbols, element names or a
    combination of the above to a list of corresponding attributes.

    Args:
      ids: list, str or int
        A list of atomic number, symbols, element names of a combination of
        them
      attr: str
        Name of the desired attribute

    Returns:
      out: list
        List of attributes corresponding to the ids
    """

    if isinstance(ids, (list, tuple)):
        return [getattr(e, attr) for e in element(ids)]
    else:
        return [getattr(element(ids), attr)]


def deltaN(
    id1: Union[str, int],
    id2: Union[str, int],
    charge1: int = 0,
    charge2: int = 0,
    missingIsZero: bool = True,
) -> Union[float, None]:
    r"""
    Calculate the approximate fraction of transferred electrons between
    elements or ions `id1` and `id2` with charges `charge1` and `charge2`
    respectively according to the expression

    .. math::

       \Delta N = \frac{\chi_{A} - \chi_{B}}{2(\eta_{A} + \eta_{B})}

    where :math:`\chi` is the Mulliken electronegativity and :math:`\eta`
    is the absolute hardness. Returns ``None`` when either quantity cannot
    be computed, i.e. when a required ionization energy or electron
    affinity is missing and ``missingIsZero`` is ``False``, or when the
    hardness is undefined for either of the elements.

    Args:
      id1: str or int
        Element identifier atomic number, symbol or element name
      id2: str or int
        Element identifier atomic number, symbol or element name
      charge1: int
        Charge of the ion formed from `id1`
      charge2: int
        Charge of the ion formed from `id2`
      missingIsZero: bool
        If ``True`` treat missing ionization energies and electron
        affinities as zero when computing the Mulliken electronegativity.
        The camelCase name is kept for backwards compatibility.
    """

    atns = ids_to_attr([id1, id2], attr="atomic_number")

    with get_session() as session:
        e1, e2 = [
            session.query(Element).filter(Element.atomic_number == a).one()
            for a in atns
        ]

    chi = [
        x.electronegativity_mulliken(charge=c, missing_is_zero=missingIsZero)
        for x, c in zip([e1, e2], [charge1, charge2])
    ]

    hardy = [e.hardness(charge=c) for e, c in zip([e1, e2], [charge1, charge2])]

    if all(x is not None for x in chi) and all(h is not None for h in hardy):
        return (chi[0] - chi[1]) / (2.0 * (hardy[0] + hardy[1]))
    else:
        return None


def get_attribute_for_all_elements(attribute: str) -> List:
    """
    Get a list of from a single attribute of all elements in the database.
    """
    engine = get_engine()
    with Session(engine) as session:
        return [
            getattr(r, attribute)
            for r in session.query(getattr(Element, attribute))
            .order_by(Element.atomic_number)
            .all()
        ]
