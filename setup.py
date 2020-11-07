# -*- coding: utf-8 -*-

"""
    Setup file for the mendeleev package.
"""

from setuptools import setup, find_packages

# Change these settings according to your needs
MAIN_PACKAGE = "mendeleev"
DESCRIPTION = "Python API with a database of atomic properties for elements in the periodic table"
LICENSE = "MIT"
URL = "https://github.com/lmmentel/mendeleev"
DOWNLOAD_URL = 'https://github.com/lmmentel/mendeleev/archive/master.zip'
AUTHOR = "Lukasz Mentel"
EMAIL = "lmmentel@gmail.com"
VERSION = '0.6.1'
KEYWORDS = ['periodic', 'table', 'elements', 'atomic', 'properties',
            'mendeleev']


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


DEPENDENCIES = ['numpy', 'pandas', 'sqlalchemy>=1.3.0', 'colorama', 'pyfiglet']


def readme():
    '''Return the contents of the README.rst file.'''
    with open('README.rst', encoding='utf8') as freadme:
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
          install_requires=DEPENDENCIES,
          keywords=KEYWORDS,
          license=LICENSE,
          long_description=readme(),
          classifiers=CLASSIFIERS,
          setup_requires=['wheel'],
          packages=find_packages(exclude=['tests', 'tests.*']),
          entry_points={
                'console_scripts': [
                    'element.py = mendeleev.cli:clielement',
                    'mdlvappdata = mendeleev.utils:get_app_data']
          },
          )


if __name__ == "__main__":
    setup_package()
