#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for the mendeleev package.
"""

from setuptools import setup, find_packages

# Change these settings according to your needs
MAIN_PACKAGE = "mendeleev"
DESCRIPTION = "Python API with a database of atomic properties for elements in the periodic table"
LICENSE = "MIT"
URL = "https://bitbucket.org/lukaszmentel/mendeleev"
DOWNLOAD_URL='https://bitbucket.org/lukaszmentel/mendeleev/get/v0.2.13.tar.gz'
AUTHOR = "Lukasz Mentel"
EMAIL = "lmmentel@gmail.com"
VERSION = '0.2.13'
KEYWORDS = ['periodic', 'table', 'elements', 'atomic', 'properties', 'mendeleev']


CLASSIFIERS = ['Development Status :: 3 - Alpha',
               'Environment :: Console',
               'Intended Audience :: Science/Research',
               'License :: OSI Approved :: MIT License',
               'Natural Language :: English',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2',
               'Programming Language :: Python :: 3',
               'Topic :: Scientific/Engineering :: Chemistry',
               'Topic :: Scientific/Engineering :: Physics']

def readme():
    '''Return the contents of the README.rst file.'''
    with open('README.rst') as freadme:
        return freadme.read()

def setup_package():

    setup(name=MAIN_PACKAGE,
          version=VERSION,
          url=URL,
          download_url=DOWNLOAD_URL,
          description=DESCRIPTION,
          author=AUTHOR,
          author_email=EMAIL,
          include_package_data=True,
          keywords=KEYWORDS,
          license=LICENSE,
          long_description=readme(),
          classifiers=CLASSIFIERS,
          packages=find_packages(exclude=['tests', 'tests.*']),
          entry_points = {
            'console_scripts' : [
                'element.py = mendeleev.mendeleev:clielement',
            ]
          },
    )

if __name__ == "__main__":
    setup_package()
