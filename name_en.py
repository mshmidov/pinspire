#!/usr/bin/env python3
import sys

__author__ = 'mshmidov'

from table.markov_table import MarkovTable

NAME_M_EN = MarkovTable(['seed/england/medieval-norman-m.txt',
                         'seed/england/medieval-norse-m.txt',
                         'seed/england/medieval-rarities-m.txt'],
                        key_size=3, prettify_result=lambda line: line.title(), exclude_exact_matches=True, limit=10)

NAME_F_EN = MarkovTable(['seed/england/medieval-norman-f.txt',
                         'seed/england/medieval-norse-f.txt',
                         'seed/england/medieval-rarities-f.txt'],
                        key_size=3, prettify_result=lambda line: line.title(), exclude_exact_matches=True, limit=10)

SURNAME_EN = MarkovTable(['seed/england/old-english-surnames.txt',
                          'seed/england/trade-surnames.txt',
                          'seed/england/byname-surnames.txt'],
                         key_size=3, prettify_result=lambda line: line.title(), exclude_exact_matches=True)


def english_name(male=True):
    name_chain = NAME_M_EN if male else NAME_F_EN

    name = [name_chain.roll(), SURNAME_EN.roll()]

    return " ".join(name)


if __name__ == '__main__':
    female = len(sys.argv) > 1 and sys.argv[1] == '-f'

    print(english_name(not female))
