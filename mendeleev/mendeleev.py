# -*- coding: utf-8 -*-

from typing import Union

import six

from .db import get_session
from .models import Element


__all__ = [
    "get_all_elements",
    "element",
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
    elif isinstance(ids, (six.string_types, int)):
        return _get_element(ids)
    else:
        raise ValueError(
            "Expected a <list>, <tuple>, <str> or <int>, got: {0:s}".format(type(ids))
        )


def _get_element(ids):
    """
    Return an element from the database based on the `ids` identifier passed.
    Valid identifiers for an element are: *name*, *symbol*, *atomic number*.
    """

    session = get_session()

    if isinstance(ids, six.string_types):
        if len(ids) <= 3 and ids.lower() != "tin":
            return session.query(Element).filter(Element.symbol == str(ids)).one()
        else:
            return session.query(Element).filter(Element.name == str(ids)).one()
    elif isinstance(ids, int):
        return session.query(Element).filter(Element.atomic_number == ids).one()
    else:
        raise ValueError("Expecting a <str> or <int>, got: {0:s}".format(type(ids)))


def get_all_elements():
    "Get all elements as a list"

    session = get_session()
    elements = session.query(Element).all()
    session.close()
    return elements


def ids_to_attr(ids, attr="atomic_number"):
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


def deltaN(id1, id2, charge1=0, charge2=0, missingIsZero=True):
    """
    Calculate the approximate fraction of transferred electrons between
    elements or ions `id1` and `id2` with charges `charge1` and `charge2`
    respectively according to the expression

    .. math::

       \Delta N = \\frac{\chi_{A} - \chi_{B}}{2(\eta_{A} + \eta_{B})}

    Args:
      id1: str or int
        Element identifier atomic number, symbol or element name
      id2: str or int
        Element identifier atomic number, symbol or element name
    """

    session = get_session()
    atns = ids_to_attr([id1, id2], attr="atomic_number")

    e1, e2 = [
        session.query(Element).filter(Element.atomic_number == a).one() for a in atns
    ]

    chi = [
        x.en_mulliken(charge=c, missingIsZero=missingIsZero)
        for x, c in zip([e1, e2], [charge1, charge2])
    ]

    if all(x is not None for x in chi):
        return (chi[0] - chi[1]) / (
            2.0 * (e1.hardness(charge=charge1) + e2.hardness(charge=charge2))
        )
    else:
        return None
