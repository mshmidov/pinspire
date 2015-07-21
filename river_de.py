#!/usr/bin/env python3

from table.markovchain import MarkovChain, ExcludeSourceElements

__author__ = 'mshmidov'

RIVER_DE = ExcludeSourceElements(MarkovChain())
RIVER_DE.populate_from(line.casefold().strip() for line in open('seed/river_de.txt'))

if __name__ == '__main__':
    print(RIVER_DE.sequence().title())
