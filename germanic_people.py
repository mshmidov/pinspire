#!/usr/bin/env python3

from engine.util import most_popular

__author__ = 'mshmidov'

from engine.markovchain import MarkovChain, ExcludeSourceElements, FilterByPredicate

GERMANIC_PEOPLE = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 4)
GERMANIC_PEOPLE.populate_from(line.casefold().strip() for line in open('seed/germanic_people.txt'))

if __name__ == '__main__':

    for people, count in most_popular(lambda: GERMANIC_PEOPLE.sequence().title(), count=70, runs=100000):
        print("{}: {}".format(people, count))
