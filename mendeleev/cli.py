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

import argparse
import textwrap
import colorama
from pyfiglet import Figlet
from colorama import Fore
from mendeleev import element, get_table


def clielement():
    '''
    CLI for convenient printing of properties for a given element
    '''

    colorama.init(autoreset=True)

    parser = argparse.ArgumentParser()
    parser.add_argument('element',
        help='Element identifier: symbol, name or atomic number')
    args = parser.parse_args()

    try:
        args.element = int(args.element)
    except ValueError:
        pass

    e = element(args.element)

    f = Figlet('dotmatrix', justify='center')
    symbol = f.renderText(e.symbol)

    table = get_table('elements')
    et = table[table['symbol'] == e.symbol].transpose()
    et.drop('description', inplace=True)
    et.drop('sources', inplace=True)
    et.drop('uses', inplace=True)

    et.index = et.index.str.replace('_', ' ').str.capitalize()
    et.sort_index(inplace=True)

    # print the data

    print(Fore.RED + symbol)

    if e.description is not None:
        print(Fore.BLUE + 'Description\n===========\n')
        print('\n'.join(['  ' + s for s in textwrap.wrap(e.description, 70)]))

    if e.sources is not None:
        print(Fore.BLUE + '\nSources\n=======\n')
        print('\n'.join(['  ' + s for s in textwrap.wrap(e.sources, 70)]))

    if e.uses is not None:
        print(Fore.BLUE + '\nUses\n====\n')
        print('\n'.join(['  ' + s for s in textwrap.wrap(e.uses, 70)]))

    print(Fore.GREEN + '\nProperties\n==========\n')
    print(et.to_string(justify='left', header=False))


if __name__ == "__main__":

    clielement()
