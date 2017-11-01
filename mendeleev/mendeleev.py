# -*- coding: utf-8 -*-

#The MIT License (MIT)
#
#Copyright (c) 2015 Lukasz Mentel
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from __future__ import print_function

import os

import numpy as np
import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import sqlite

import six

from .tables import Base, Element, IonizationEnergy


def get_session():
    '''Return the database session connection.'''

    dbpath = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                          "elements.db")
    engine = create_engine("sqlite:///{path:s}".format(path=dbpath),
                           echo=False)
    db_session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    return db_session()


def get_engine():
    '''Return the db engine'''

    dbpath = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                          "elements.db")
    engine = create_engine("sqlite:///{path:s}".format(path=dbpath),
                           echo=False)
    return engine


def element(ids):
    '''
    Based on the type of the `ids` identifier return either an
    :py:class:`Element <mendeleev.tables.Element>` object from the
    database, or a list of :py:class:`Element <mendeleev.tables.Element>`
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

    '''

    if isinstance(ids, (list, tuple)):
        return [_get_element(i) for i in ids]
    elif isinstance(ids, (six.string_types, int)):
        return _get_element(ids)
    else:
        raise ValueError("Expected a <list>, <tuple>, <str> or <int>, got: {0:s}".format(type(ids)))


def _get_element(ids):
    '''
    Return an element from the database based on the `ids` identifier passed.
    Valid identifiers for an element are: *name*, *symbol*, *atomic number*.
    '''

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
    'Get all elements as a list'

    session = get_session()
    elements = session.query(Element).all()
    session.close()
    return elements


def get_table(tablename, **kwargs):
    '''
    Return a table from the database as `pandas <http://pandas.pydata.org/>`_
    `DataFrame <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html>`_

    Args:
      tablename: str
        Name of the table from the database
      kwargs:
        A dictionary of keyword arguments to pass to the `pandas.read_qsl`

    Returns:
      df: pandas.DataFrame
        Pandas DataFrame with the contents of the table

    Example:
        >>> from mendeleev import get_table
        >>> df = get_table('elements')
        >>> type(df)
        pandas.core.frame.DataFrame

    '''

    tables = ['elements', 'isotopes', 'ionicradii', 'ionizationenergies',
              'groups', 'series', 'oxidationstates']

    if tablename in tables:
        engine = get_engine()
        dframe = pd.read_sql(tablename, engine, **kwargs)
        return dframe
    else:
        raise ValueError('Table should be one of: {}'.format(", ".join(tables)))


def get_attr_for_group(attr, group=18):
    '''
    A convenience function for getting a specified attribute for all
    the memebers of a given group.

    Args:
        attr : str
            Attribute of `Element` to retrieve for all the noble gasses

    Returns:
        data : dict
            Dictionary with nobel gas atomic numbers as keys and values of the
            `attr` as values
    '''

    session = get_session()
    ngs = session.query(Element).filter(Element.group_id == group).all()
    x = np.array([ng.atomic_number for ng in ngs])
    y = np.array([getattr(ng, attr) for ng in ngs])
    session.close()
    return x, y


def ids_to_attr(ids, attr='atomic_number'):
    '''
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
    '''

    if isinstance(ids, (list, tuple)):
        return [getattr(e, attr) for e in element(ids)]
    else:
        return [getattr(element(ids), attr)]


def get_ips(ids=None, deg=1):
    '''
    Return a pandas DataFrame with ionization energies for a set of elements.

    Args:
      ids: list, str or int
        A list of atomic number, symbols, element names of a combination of the
        above. If nothing is specified all elements are selected.
      deg: int or list of int
        Degree of ionization, either as int or a list of ints. If a list is
        passed then the output will contain ionization energies corresponding
        to particalr degrees in columns.

    Returns:
      df: DataFrame
        Pandas DataFrame with atomic numbers, symbols and ionization energies
    '''

    session = get_session()
    engine = get_engine()

    if ids is None:
        atns = list(range(1, 119))
    else:
        atns = ids_to_attr(ids, attr='atomic_number')

    query = session.query(Element.atomic_number, Element.symbol).filter(Element.atomic_number.in_(atns))
    df = pd.read_sql_query(query.statement.compile(dialect=sqlite.dialect()), engine)

    if isinstance(deg, (list, tuple)):
        if all(isinstance(d, int) for d in deg):
            for d in deg:
                query = session.query(IonizationEnergy).\
                            filter(IonizationEnergy.degree == d).\
                            filter(IonizationEnergy.atomic_number.in_((atns)))
                out = pd.read_sql_query(query.statement.compile(dialect=sqlite.dialect()), engine)
                out = out[['atomic_number', 'energy']]
                out.columns = ['atomic_number', 'IP{0:d}'.format(d)]
                df = pd.merge(df, out, on='atomic_number', how='left')
        else:
            raise ValueError('deg should be a list of ints')
    elif isinstance(deg, int):
        query = session.query(IonizationEnergy).\
                    filter(IonizationEnergy.degree == deg).\
                    filter(IonizationEnergy.atomic_number.in_((atns)))
        out = pd.read_sql_query(query.statement.compile(dialect=sqlite.dialect()), engine)
        out = out[['atomic_number', 'energy']]
        out.columns = ['atomic_number', 'IP{0:d}'.format(deg)]
        df = pd.merge(df, out, on='atomic_number', how='left')
    else:
        raise ValueError('deg should be an int or a list or tuple of ints')

    return df


def get_ionic_radii(values='ionic_radius'):
    '''
    Return a pandas DataFrame with ionic radii for a set of elements.

    Args:
      values : str
        The values to be returned either `ionic_radius` or `crystal_radius`

    Returns:
      df: DataFrame
        Pandas DataFrame with atomic numbers, symbols and ionic radii for all
        coordinations
    '''

    if values not in ['ionic_radius', 'crystal_radius']:
        raise ValueError('wrong values, should be "ionic_radius" or "crystal_radius"')

    ir = get_table('ionicradii')
    ir = ir[ir.spin != 'HS']
    # create new temporary pseudo multiindex
    ir['idx'] = ir.atomic_number.astype(str) + '(' + ir.charge.astype(str) + ')'
    df = ir.pivot(index='idx', columns='coordination', values='ionic_radius')
    # get back the atomic_number and charge columns from idx
    df['atomic_number'] = df.index.str.extract(r'^(\d+)')
    df['charge'] = df.index.str.extract(r'^\d+\((-?\d+)\)')
    df.reset_index(inplace=True)
    df.drop('idx', axis=1, inplace=True)

    return df


def deltaN(id1, id2, charge1=0, charge2=0, missingIsZero=True):
    '''
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
    '''

    session = get_session()
    atns = ids_to_attr([id1, id2], attr='atomic_number')

    e1, e2 = [session.query(Element).filter(Element.atomic_number == a).one()
              for a in atns]

    chi = [x.en_mulliken(charge=c, missingIsZero=missingIsZero)
           for x, c in zip([e1, e2], [charge1, charge2])]

    if all(x is not None for x in chi):
        return (chi[0] - chi[1]) / (2.0 * (e1.hardness(charge=charge1) +
                                           e2.hardness(charge=charge2)))
    else:
        return None


def attributes(elem, names, fmt='8.3f'):
    '''
    Return a list of strings of all the attributes of ``elem`` specified in
    ``names``
    '''

    return ['\t{0:s} = {1:{fmt}}'.format(name.replace('_', ' ').capitalize(),
                                         getattr(elem, name), fmt=fmt)
                                         for name in names]


def n_eff(n):
    '''Return the effective principal quantum number

    Args:
        n : (int)
            Principal quantum number

    .. note::
       The values are taken from J. A. Pople, D. L. Beveridge,
       "Approximate Molecular Orbital Theory", McGraw-Hill, 1970
    '''

    values = {1: 1.0, 2: 2.0, 3: 3.0, 4: 3.7, 5: 4.0, 6: 4.2}

    return values.get(n, None)
