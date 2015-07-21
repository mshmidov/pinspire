#!/usr/bin/env python3

from engine.util import name_generator_by_argparse

__author__ = 'mshmidov'

from engine.markovchain import MarkovChain, ExcludeSourceElements, FilterByPredicate

GERMANIC_PEOPLE = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 4)
GERMANIC_PEOPLE.populate_from(line.casefold().strip() for line in open('seed/germanic_people.txt'))

if __name__ == '__main__':
    name_generator_by_argparse({'people': lambda: GERMANIC_PEOPLE.sequence().title()})

