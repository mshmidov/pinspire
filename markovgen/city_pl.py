#!/usr/bin/env python3

from engine.util import name_generator_by_argparse
from engine.markovchain import MarkovChain, ExcludeSourceElements, FilterByPredicate

CITY_PL = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 3)
CITY_PL.populate_from(line.casefold().strip() for line in open('seed/cities/city_pl.txt'))

if __name__ == '__main__':
    name_generator_by_argparse({'city': lambda: CITY_PL.sequence().title()})
