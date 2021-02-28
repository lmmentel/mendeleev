# -*- coding: utf-8 -*-

from __future__ import print_function

import argparse
import textwrap
import colorama
from pyfiglet import Figlet
from mendeleev import element
from mendeleev.fetch import fetch_table


def clielement():
    """
    CLI for convenient printing of properties for a given element
    """

    colorama.init(autoreset=True)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "element", help="Element identifier: symbol, name or atomic number"
    )
    args = parser.parse_args()

    try:
        args.element = int(args.element)
    except ValueError:
        pass

    e = element(args.element)

    f = Figlet("dotmatrix", justify="center")
    symbol = f.renderText(e.symbol)

    table = fetch_table("elements")
    et = table[table["symbol"] == e.symbol].transpose()
    et.drop("description", inplace=True)
    et.drop("sources", inplace=True)
    et.drop("uses", inplace=True)

    et.index = et.index.str.replace("_", " ").str.capitalize()
    et.sort_index(inplace=True)

    # print the data

    print(colorama.Fore.RED + symbol)

    if e.description is not None:
        print(colorama.Fore.BLUE + "Description\n===========\n")
        print("\n".join("  " + s for s in textwrap.wrap(e.description, 70)))

    if e.sources is not None:
        print(colorama.Fore.BLUE + "\nSources\n=======\n")
        print("\n".join("  " + s for s in textwrap.wrap(e.sources, 70)))

    if e.uses is not None:
        print(colorama.Fore.BLUE + "\nUses\n====\n")
        print("\n".join("  " + s for s in textwrap.wrap(e.uses, 70)))

    print(colorama.Fore.GREEN + "\nProperties\n==========\n")
    print(et.to_string(justify="left", header=False))


if __name__ == "__main__":

    clielement()
