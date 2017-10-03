
# inspirations

# https://stackoverflow.com/questions/1462986/lazy-module-variables-can-it-be-done
# https://codereview.stackexchange.com/questions/10481/lazy-class-instantiation-in-python
# https://stackoverflow.com/questions/15226721/python-class-member-lazy-initialization
# https://stackoverflow.com/questions/7151890/python-lazy-variables-or-delayed-expensive-computation

# https://stackoverflow.com/a/1950986
# https://stackoverflow.com/questions/28607701/is-it-possible-to-recover-import-after-overwriting-it

_symbols = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
            'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
            'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
            'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr',
            'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn',
            'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd',
            'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb',
            'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
            'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
            'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm',
            'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds',
            'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']


#globals().update({k: None for k in _symbols})

import builtins

def custom_import(name, globals=None, locals=None, fromlist=(), level=0):

    print('importing: ', name, fromlist)

    for item_name in fromlist:
        if item_name not in _symbols:
            raise ImportError('{} is not an element symbol.'.format(item_name))

    return


builtins.__import__ = custom_import



#__all__ = _symbols
