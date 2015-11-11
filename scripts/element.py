# -*- coding: utf-8 -*-

from __future__ import print_function

import argparse
import textwrap
from mendeleev import element, get_table
from pyfiglet import Figlet

#write units

def attributes(elem, names, fmt='8.3f'):

    return ['\t{0:s} = {1:{fmt}}'.format(name.replace('_', ' ').capitalize(), getattr(elem, name), fmt=fmt) for name in names]

def main():

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

    print(header, desc, props, et.to_string(justify='left', header=False), sep='\n')

if __name__ == '__main__':
    main()
