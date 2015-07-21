#!/usr/bin/env python3
__author__ = 'mshmidov'
import sys

from engine.util import most_popular

from engine.markovchain import MarkovChain, ExcludeSourceElements, FilterByPredicate

NAME_M_RU = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 4)
NAME_M_RU.populate_from(line.casefold().strip() for line in open('seed/russia/names-slavic-m.txt'))
NAME_M_RU.populate_from(line.casefold().strip() for line in open('seed/russia/names-russia-latin-m.txt'))

NAME_F_RU = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 4)
NAME_F_RU.populate_from(line.casefold().strip() for line in open('seed/russia/names-slavic-f.txt'))
NAME_F_RU.populate_from(line.casefold().strip() for line in open('seed/russia/names-russia-latin-f.txt'))


def russian_name(male=True):
    name_chain = NAME_M_RU if male else NAME_F_RU

    return name_chain.sequence().title()


if __name__ == '__main__':
    female = len(sys.argv) > 1 and sys.argv[1] == '-f'

    for name, count in most_popular(lambda: russian_name(not female), count=40, runs=100000):
        print("{}: {}".format(name, count))
