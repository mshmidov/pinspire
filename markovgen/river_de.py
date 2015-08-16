#!/usr/bin/env python3

from engine.markovchain import MarkovChain, ExcludeSourceElements, FilterByPredicate
from engine.util import name_generator_by_argparse

__author__ = 'mshmidov'

RIVER_DE = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 3)
RIVER_DE.populate_from(line.casefold().strip() for line in open('seed/rivers/river_de.txt'))

if __name__ == '__main__':
    name_generator_by_argparse({'river': lambda: RIVER_DE.sequence().title()})
