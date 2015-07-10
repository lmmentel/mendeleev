========
elements
========

A periodic table of elements database with a python interface.

Dependencies
============

* SQLAlchemy_

.. _SQLalchemy: http://www.sqlalchemy.org

Installation
============

After downloading and unpacking enter the ``elements`` directory and install by

.. code-block:: bash

   python setup.py install [--user]

Usage
=====

For simple access to the database there is the ``element`` method that accepts
either the atomic symbol, atomic number, element name or a list of composed
of those identifiers. The method return either a single ``Element`` object or
a list of the dependent on the input.

.. code-block:: python

    >>> from elements import element
    >>> h = element('H')
    >>> h
    Element(
        annotation='density(@ -253C), evaporation_heat(H-H), fusion_heat(H-H), ',
        atomic_number=1,
        atomic_radius=79.0,
        atomic_volume=14.1,
        block='s',
        boiling_point=20.28,
        covalent_radius=32.0,
        density=0.0708,
        description='Colourless, odourless gaseous chemical element. Lightest and most abundant element in the universe. Present in water and in all organic compounds. Chemically reacts with most elements. Discovered by Henry Cavendish in 1776.',
        dipole_polarizability=4.50710742367,
        electron_affinity=0.75420375,
        electronegativity=2.2,
        electronic_configuration='1s',
        evaporation_heat=0.904,
        fusion_heat=0.117,
        group_id=1,
        lattice_constant=3.75,
        lattice_structure='HEX',
        mass=1.00794,
        melting_point='14.01',
        name='Hydrogen',
        period=1,
        specific_heat=None,
        symbol='H',
        thermal_conductivity=0.1815,
        vdw_radius=1.2,
    )


Documentation
=============

.. image:: https://readthedocs.org/projects/elements/badge/
   :target: https://elements.readthedocs.org/en/latest/
   :alt: Documentation Status

Documentation can be found `here <http://elements.readthedocs.org/en/latest/>`_.


License
=======

| The MIT License (MIT)
|
| Copyright (c) 2015 Lukasz Mentel
|
| Permission is hereby granted, free of charge, to any person obtaining a copy
| of this software and associated documentation files (the "Software"), to deal
| in the Software without restriction, including without limitation the rights
| to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
| copies of the Software, and to permit persons to whom the Software is
| furnished to do so, subject to the following conditions:
|
| The above copyright notice and this permission notice shall be included in all
| copies or substantial portions of the Software.
|
| THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
| IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
| FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
| AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
| LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
| OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
| SOFTWARE.

