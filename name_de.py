#!/usr/bin/env python3
import sys

__author__ = 'mshmidov'

from table.markov_table import MarkovTable

NAME_M_DE = MarkovTable(['seed/europe/names-germanic-m.txt',
                         'seed/europe/names-low-german-m.txt',
                         'seed/europe/names-medieval-germany-m.txt'],
                        key_size=3, prettify_result=lambda line: line.title(), exclude_exact_matches=True, limit=10)

NAME_F_DE = MarkovTable(['seed/europe/names-germanic-f.txt',
                         'seed/europe/names-low-german-f.txt',
                         'seed/europe/names-medieval-germany-f.txt'],
                        key_size=3, prettify_result=lambda line: line.title(), exclude_exact_matches=True, limit=10)

SURNAME_DE = MarkovTable(['seed/europe/surnames-germany.txt'],
                         key_size=3, prettify_result=lambda line: line.title(), exclude_exact_matches=True)


def german_name(male=True):
    name_chain = NAME_M_DE if male else NAME_F_DE

    name = [name_chain.roll(), SURNAME_DE.roll()]

    return " ".join(name)


if __name__ == '__main__':
    female = len(sys.argv) > 1 and sys.argv[1] == '-f'

    print(german_name(not female))
