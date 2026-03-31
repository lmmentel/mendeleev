.. _units:

****************************
Working with Physical Units
****************************

.. versionadded:: 1.1.0

As of version 1.1.0, mendeleev integrates with the `pint <https://pint.readthedocs.io/>`_
library for proper handling of physical units and quantities. This allows you to work with
element properties in a unit-aware manner, making conversions easier and reducing errors
in calculations.

Overview
========

The integration with pint provides:

- **Unit-aware properties**: Physical properties are returned with their proper units
- **Automatic conversions**: Easy conversion between different unit systems
- **Dimensional analysis**: Ensures calculations are dimensionally correct
- **Type safety**: Prevents mixing incompatible units

Getting Property Metadata
==========================

You can access metadata about properties, including their units, using the
:py:func:`fetch_table <mendeleev.fetch.fetch_table>` function::

    >>> from mendeleev import fetch_table
    >>> metadata = fetch_table('propertymetadata')
    >>> # View properties with their units
    >>> metadata[['attribute_name', 'unit']].head(10)

This shows the units associated with each element property.

Available Units
===============

Common units used in mendeleev include:

**Length/Distance:**
  - ``pm`` (picometers) - atomic and ionic radii
  - ``bohr`` - Bohr radius units

**Energy:**
  - ``eV`` (electron volts) - ionization energies, electron affinities
  - ``hartree`` - atomic units of energy

**Temperature:**
  - ``K`` (Kelvin) - melting points, boiling points

**Pressure:**
  - ``MPa`` (megapascals) - critical pressure

**Mass:**
  - ``Da`` (Daltons) - atomic weights
  - ``g/cm^3`` - density

**Other:**
  - ``mg/kg`` - abundance in Earth's crust
  - ``mg/L`` - abundance in seas
  - ``cm^3/mol`` - atomic volume

Working with Units
==================

Basic Usage
-----------

Element properties that have units are stored in the database with their unit information.
The property metadata table contains this information::

    >>> from mendeleev import element
    >>> si = element('Si')
    >>> # Access properties - units depend on the property
    >>> si.atomic_radius  # in pm (picometers)
    132
    >>> si.boiling_point  # in K (Kelvin)
    2628

Converting Units
----------------

For unit conversions and dimensional analysis, you can use the pint library directly::

    >>> import pint
    >>> ureg = pint.UnitRegistry()
    >>>
    >>> # Convert atomic radius from pm to Angstroms
    >>> radius_pm = 132 * ureg.pm
    >>> radius_angstrom = radius_pm.to(ureg.angstrom)
    >>> print(radius_angstrom)
    1.32 angstrom
    >>>
    >>> # Convert boiling point from K to Celsius
    >>> bp_kelvin = 2628 * ureg.K
    >>> bp_celsius = bp_kelvin.to(ureg.degC)
    >>> print(bp_celsius)
    2354.85 degree_Celsius

Unit-Aware Calculations
-----------------------

Using pint ensures dimensional correctness in calculations::

    >>> import pint
    >>> ureg = pint.UnitRegistry()
    >>>
    >>> # Calculate volume from radius (spherical approximation)
    >>> from mendeleev import element
    >>> import math
    >>>
    >>> si = element('Si')
    >>> radius = si.atomic_radius * ureg.pm
    >>> volume = (4/3) * math.pi * radius**3
    >>> print(volume.to('angstrom**3'))
    9.6 angstrom ** 3

Property Metadata Reference
============================

The ``PropertyMetadata`` table contains comprehensive information about all stored properties:

- ``attribute_name``: The property name as accessed in code
- ``unit``: The unit of measurement (if applicable)
- ``description``: Human-readable description
- ``value_origin``: Whether the value is stored or computed
- ``citation_keys``: References to source publications

You can query this metadata to understand what units are used for each property::

    >>> from mendeleev import fetch_table
    >>> metadata = fetch_table('propertymetadata')
    >>>
    >>> # Find all properties with energy units
    >>> energy_props = metadata[metadata['unit'].str.contains('eV', na=False)]
    >>> print(energy_props[['attribute_name', 'unit', 'description']])

See Also
========

- :doc:`Data reference <data>` - Complete list of available properties
- :doc:`Data access <data_access>` - How to fetch and query data
- `pint documentation <https://pint.readthedocs.io/>`_ - Full pint library documentation

.. note::
   While mendeleev integrates with pint for unit support, most properties are still
   returned as numeric values in their documented units. Full pint Quantity objects
   may be added in future versions for more seamless unit handling.
