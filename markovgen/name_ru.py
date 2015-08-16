#!/usr/bin/env python3

from engine.util import name_generator_by_argparse
from engine.markovchain import MarkovChain, ExcludeSourceElements, FilterByPredicate

NAME_M_RU = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 3)
NAME_M_RU.populate_from(line.casefold().strip() for line in open('seed/names/russia/names-slavic-m.txt'))
NAME_M_RU.populate_from(line.casefold().strip() for line in open('seed/names/russia/names-russia-latin-m.txt'))

NAME_F_RU = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 3)
NAME_F_RU.populate_from(line.casefold().strip() for line in open('seed/names/russia/names-slavic-f.txt'))
NAME_F_RU.populate_from(line.casefold().strip() for line in open('seed/names/russia/names-russia-latin-f.txt'))

if __name__ == '__main__':
    name_generator_by_argparse({'male': lambda: NAME_M_RU.sequence().title(),
                                'female': lambda: NAME_F_RU.sequence().title()})
