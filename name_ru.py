#!/usr/bin/env python3
__author__ = 'mshmidov'
import sys

from table.markovchain import MarkovChain, ExcludeSourceElements

NAME_M_RU = ExcludeSourceElements(MarkovChain())
NAME_M_RU.populate_from(line.casefold().strip() for line in open('seed/russia/names-slavic-m.txt'))
NAME_M_RU.populate_from(line.casefold().strip() for line in open('seed/russia/names-russia-latin-m.txt'))

NAME_F_RU = ExcludeSourceElements(MarkovChain())
NAME_F_RU.populate_from(line.casefold().strip() for line in open('seed/russia/names-slavic-f.txt'))
NAME_F_RU.populate_from(line.casefold().strip() for line in open('seed/russia/names-russia-latin-f.txt'))


def russian_name(male=True):
    name_chain = NAME_M_RU if male else NAME_F_RU

    name = [name_chain.sequence().title()]

    return " ".join(name)


if __name__ == '__main__':
    female = len(sys.argv) > 1 and sys.argv[1] == '-f'

    for _ in range(10):
        print(russian_name(not female))
