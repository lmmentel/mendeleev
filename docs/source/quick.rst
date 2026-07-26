.. _quick-start:

***********
Quick Start
***********

Install mendeleev (see :doc:`install` for details):

.. code-block:: bash

   pip install mendeleev

Or with visualization support:

.. code-block:: bash

   pip install mendeleev[vis]

All examples below work after ``pip install mendeleev``. No database download needed — it ships with the package.

----

1. Get an element by symbol
===========================

.. code-block:: python

   from mendeleev import element

   si = element("Si")
   print(si.name)           # Silicon
   print(si.atomic_number)  # 14

2. Get an element by name or atomic number
===========================================

.. code-block:: python

   from mendeleev import element

   al = element("Aluminium")   # by name
   o  = element(8)             # by atomic number
   print(al.atomic_number)     # 13
   print(o.name)               # Oxygen

3. Import elements directly by symbol
======================================

.. code-block:: python

   from mendeleev import Fe, O, H

   print(Fe.name)           # Iron
   print(H.atomic_weight)   # 1.008

4. Get multiple elements at once
=================================

.. code-block:: python

   from mendeleev import element

   c, h, o = element(["C", "Hydrogen", 8])
   print(c.name, h.name, o.name)  # Carbon Hydrogen Oxygen

5. Access element properties
=============================

.. code-block:: python

   from mendeleev import element

   si = element("Si")
   print(f"Atomic weight:      {si.atomic_weight}  Da")
   print(f"Melting point:      {si.melting_point}  K")
   print(f"Boiling point:      {si.boiling_point}  K")
   print(f"Density:            {si.density}        g/cm³")
   print(f"Electronegativity:  {si.en_pauling}")
   print(f"Electron affinity:  {si.electron_affinity}  eV")

6. Work with isotopes
=====================

.. code-block:: python

   from mendeleev import element

   carbon = element("C")
   for iso in carbon.isotopes:
       print(f"C-{iso.mass_number}: {iso.abundance}%")
   # C-12: 98.93%
   # C-13: 1.07%

Access a specific isotope directly:

.. code-block:: python

   from mendeleev import isotope

   c14 = isotope("C", 14)
   print(f"Half-life: {c14.half_life} years")  # 5700.0

7. Bulk data with pandas
=========================

.. code-block:: python

   from mendeleev import fetch_table

   df = fetch_table("elements")
   print(df[["symbol", "name", "atomic_number", "atomic_weight"]].head())

   # Filter and sort
   heavy = df[df["atomic_number"] > 80]
   print(heavy[["symbol", "name", "density"]].sort_values("density", ascending=False))

8. Create a visualization
==========================

.. code-block:: python

   from mendeleev.vis import periodic_table

   # Interactive plot (requires bokeh or plotly)
   periodic_table(colorby="atomic_radius", backend="plotly")

   # Save a static plot
   periodic_table(colorby="en_pauling", backend="seaborn", output="en_periodic.png")

9. Work with ions
=================

.. code-block:: python

   from mendeleev.ion import Ion

   fe2 = Ion("Fe", charge=2)
   fe3 = Ion("Fe", charge=3)
   print(f"Ionic radius Fe²⁺: {fe2.ionic_radius} pm")
   print(f"Ionic radius Fe³⁺: {fe3.ionic_radius} pm")

10. Compare electronegativity scales
=====================================

.. code-block:: python

   from mendeleev import fetch_electronegativities

   en = fetch_electronegativities(["pauling", "allen", "mulliken"])
   print(en[en["symbol"] == "Si"])

Or access scales directly on an element:

.. code-block:: python

   from mendeleev import element

   si = element("Si")
   print(si.en_pauling)       # 1.9
   print(si.en_allen)         # 11.33
   print(si.en_mulliken())    # computed on the fly

11. Access properties with units
=================================

.. code-block:: python

   from mendeleev import Fe, Al

   # Append _u to any property for a pint Quantity
   print(Fe.atomic_weight_u)   # 55.845 dalton
   print(Al.melting_point_u)   # 933.47 kelvin

   # Convert units easily
   print(Al.melting_point_u.to("celsius"))  # 660.32 degree_Celsius

12. Use the CLI
===============

.. code-block:: bash

   element.py Si           # by symbol
   element.py 14           # by atomic number
   element.py Silicon      # by name

Prints all available properties in the terminal (installed with the package).


What next?
=========

* :doc:`api_overview` — choose the right function for your task
* :doc:`tutorials` — Jupyter notebook tutorials
* :doc:`data` — full list of 100+ available properties
* :doc:`faq` — frequently asked questions
* :doc:`troubleshooting` — common issues and solutions
* :doc:`citing` — citation formats and BibTeX entries
