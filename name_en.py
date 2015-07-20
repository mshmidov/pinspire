#!/usr/bin/env python3
import sys

__author__ = 'mshmidov'

from table.markov_table import MarkovTable

NAME_M_EN = MarkovTable(['seed/england/names-medieval-norman-m.txt',
                         'seed/england/names-medieval-norse-m.txt',
                         'seed/england/names-medieval-rarities-m.txt'],
                        key_size=3,
                        exclude_exact_matches=True)

NAME_F_EN = MarkovTable(['seed/england/names-medieval-norman-f.txt',
                         'seed/england/names-medieval-norse-f.txt',
                         'seed/england/names-medieval-rarities-f.txt'],
                        key_size=3,
                        exclude_exact_matches=True)

SURNAME_EN = MarkovTable(['seed/england/surnames-old-english.txt',
                          'seed/england/surnames-trade.txt',
                          'seed/england/surnames-byname.txt'],
                         key_size=3,
                         exclude_exact_matches=True)


def english_name(male=True):
    name_chain = NAME_M_EN if male else NAME_F_EN

    name = [name_chain.roll(), SURNAME_EN.roll()]

    return " ".join(name)


if __name__ == '__main__':
    female = len(sys.argv) > 1 and sys.argv[1] == '-f'

    print(english_name(not female))
