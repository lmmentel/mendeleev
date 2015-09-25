# -*- coding: utf-8 -*-

from __future__ import print_function

import argparse
import textwrap
from mendeleev import element

#write units

def attributes(elem, names, fmt='8.3f'):

    return ['\t{0:s} = {1:{fmt}}'.format(name.replace('_', ' ').capitalize(), getattr(elem, name), fmt=fmt) for name in names]

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('element', help='Element identifier: symbol, name or atomic number')
    #parser.add_argument('-f', help='Full information')
    args = parser.parse_args()

    e = element(args.element)

    headtitle = '{0:<15s}{1:<15s}{2:<15s}'.format('Atomic number', 'Name', 'Symbol')
    headvalue = '{0:<15d}{1:<15s}{2:<15s}'.format(e.atomic_number, e.name, e.symbol)

    radii = 'Radii:\n'  

    desc = 'Description:\n' + '\n'.join(['\t' + s for s in textwrap.wrap(e.description, 70)])

    print(headtitle, headvalue, desc, sep='\n')

if __name__ == '__main__':
    main()
