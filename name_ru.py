#!/usr/bin/env python3
import sys

from transliterate import translit

__author__ = 'mshmidov'

from table.markov_table import MarkovTable, prepare_line


def prepare_and_transliterate(line):
    return translit(prepare_line(line), 'ru', reversed=True)


NAME_M_RU = MarkovTable(['seed/russia/names-slavic-m.txt',
                         'seed/russia/names-russia-latin-m.txt'],
                        key_size=3,
                        exclude_exact_matches=True)

NAME_F_RU = MarkovTable(['seed/russia/names-slavic-f.txt',
                         'seed/russia/names-russia-latin-f.txt'],
                        key_size=3,
                        exclude_exact_matches=True)


# SURNAME_RU = MarkovTable(['seed/europe/surnames-germany.txt'],
#                          key_size=3, prettify_result=lambda line: line.title(), exclude_exact_matches=True)


def russian_name(male=True):
    name_chain = NAME_M_RU if male else NAME_F_RU

    name = [name_chain.roll()]

    return " ".join(name)


if __name__ == '__main__':
    female = len(sys.argv) > 1 and sys.argv[1] == '-f'

    for _ in range(10):
        print(russian_name(not female))
