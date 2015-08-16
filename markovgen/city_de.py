#!/usr/bin/env python3

from engine.util import name_generator_by_argparse
from engine.markovchain import MarkovChain, ExcludeSourceElements, FilterByPredicate

CITY_DE = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 4)
CITY_DE.populate_from(line.casefold().strip() for line in open('seed/cities/city_de.txt'))

if __name__ == '__main__':
    name_generator_by_argparse({'city': lambda: CITY_DE.sequence().title()})
