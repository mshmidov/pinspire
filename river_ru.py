#!/usr/bin/env python3

from engine.util import name_generator_by_argparse
from engine.markovchain import MarkovChain, ExcludeSourceElements, FilterByPredicate

RIVER_RU = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 3)
RIVER_RU.populate_from(line.casefold().strip() for line in open('seed/rivers/river_ru.txt'))

if __name__ == '__main__':
    name_generator_by_argparse({'city': lambda: RIVER_RU.sequence().title()})
