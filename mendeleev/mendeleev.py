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
import argparse
import textwrap

import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import sqlite

import numpy as np

import six

from .tables import Base, Element, IonizationEnergy

__all__ = ['element', 'get_session', 'get_engine', 'get_table', 'ids_to_attr',
           'get_ips', 'get_ionic_radii', 'deltaN', 'get_data', 'interpolate']


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
    :py:class:`Element <mendeleev.tables.Element>` object from the database, or
    a list of :py:class:`Element <mendeleev.tables.Element>` objects if the
    `ids` is a list or a tuple of identifiers. Valid identifiers for an element
    are: *name*, *symbol*, *atomic number*.
    '''

    if isinstance(ids, (list, tuple)):
        return [get_element(i) for i in ids]
    elif isinstance(ids, (six.string_types, int)):
        return get_element(ids)
    else:
        raise ValueError("Expected a <list>, <tuple>, <str> or <int>, got: {0:s}".format(type(ids)))


def get_element(ids):
    '''
    Return an element from the database based on the `ids` identifier passed.
    Valid identifiers for an element are: *name*, *symbol*, *atomic number*.
    '''

    session = get_session()

    if isinstance(ids, six.string_types):
        if len(ids) <= 3 and ids.lower() != "tin":
            return session.query(Element).filter(Element.symbol == ids).one()
        else:
            return session.query(Element).filter(Element.name == ids).one()
    elif isinstance(ids, int):
        return session.query(Element).filter(Element.atomic_number == ids).one()
    else:
        raise ValueError("Expecting a <str> or <int>, got: {0:s}".format(type(ids)))


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
    '''

    tables = ['elements', 'isotopes', 'ionicradii', 'ionizationenergies',
              'groups', 'series', 'oxidationstates']

    if tablename in tables:
        engine = get_engine()
        dframe = pd.read_sql(tablename, engine, **kwargs)
        return dframe
    else:
        raise ValueError('Table should be one of: {}'.format(", ".join(tables)))


def get_data():
    '''
    Get extensive set of data from multiple databse tables as pandas.DataFrame
    '''

    data = get_table('elements')

    en_scales = ['allred-rochow', 'cottrell-sutton', 'gordy',
                 'martynov-batsanov', 'mulliken', 'nagle', 'sanderson']
    for scale in en_scales:
        data['en_' + scale] = [element(row.symbol).electronegativity(scale=scale) for i, row in data.iterrows()]

    for attr in ['hardness', 'softness']:
        data[attr] = [getattr(element(row.symbol), attr)() for i, row in data.iterrows()]

    # TODO: zeff, slater, clementi, series, grups, ionization energies up to a
    # values

    return data


def _get_ng_data(attribute):
    '''
    A convenience function for getting a specified attribute for all the nobel
    gases.

    Args:
        attribute : str
            Attribute of `Element` to retrieve for all the noble gasses

    Returns:
        data : dict
            Dictionary with nobel gas atomic numbers as keys and values of the
            `attribute` as values
    '''

    session = get_session()
    ngs = session.query(Element).filter(Element.series == 'Noble gases').all()
    data = {ng.atomic_number: getattr(ng, attribute) for ng in ngs}
    session.close()
    return data


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

    e1, e2 = [session.query(Element).filter(Element.atomic_number == a).one() for a in atns]

    chi = [x.en_mulliken(charge=c, missingIsZero=missingIsZero) for x, c in zip([e1, e2], [charge1, charge2])]

    if all(x is not None for x in chi):
        return (chi[0] - chi[1])/(2.0*(e1.hardness(charge=charge1) + e2.hardness(charge=charge2)))
    else:
        return None


def interpolate(key, attribute, deg=1, kind='linear'):
    '''
    Evaluate a value for `key` by interpolation or extrapolation of the data
    points in `data`.

    Args:
      key : int
        Key for which the property will be evaluated
      deg : int
        Degree of the polynomial used in the extrapolation beyond the provided
        data points
      kind : str
        Kind of the interpolation used, see docs for `numpy.interp1d`
    '''

    data = _get_ng_data(attribute)

    if min(list(data.keys())) <= key <= max(list(data.keys())):
        return np.interp([key], list(data.keys()), list(data.values()))
    else:
        if key < min(data.keys()):
            dataslice = dict(sorted(data.items(), key=lambda x: x[0])[:3])
        elif key > max(data.keys()):
            dataslice = dict(sorted(data.items(), key=lambda x: x[0])[-3:])
        fit = np.polyfit(list(dataslice.keys()), list(dataslice.values()), deg)
        fn = np.poly1d(fit)
        return fn(key)


def attributes(elem, names, fmt='8.3f'):
    '''
    Return a list of strings of all the attributes of ``elem`` specified in
    ``names``
    '''

    return ['\t{0:s} = {1:{fmt}}'.format(name.replace('_', ' ').capitalize(),
                                         getattr(elem, name), fmt=fmt) for name in names]


def clielement():
    '''
    CLI for convenient printing of properties for a given element
    '''

    from pyfiglet import Figlet

    parser = argparse.ArgumentParser()
    parser.add_argument('element', help='Element identifier: symbol, name or atomic number')
    #parser.add_argument('-f', help='Full information')
    args = parser.parse_args()

    e = element(args.element)

    f = Figlet('dotmatrix')
    header = f.renderText(e.symbol)

    table = get_table('elements')
    et = table[table['symbol'] == e.symbol].transpose()
    et.drop('description', inplace=True)
    et.index = et.index.str.replace('_', ' ').str.capitalize()
    et.sort_index(inplace=True)

    desc = 'Description\n===========\n\n' + '\n'.join(['  ' + s for s in textwrap.wrap(e.description, 70)])

    props = '\nProperties\n==========\n'

    print(header, desc, props, et.to_string(justify='left', header=False),
          sep='\n')
