#!/usr/bin/env python3
__author__ = 'mshmidov'

from table.markov_table import MarkovTable

RIVER_DE = MarkovTable(["seed/river_de.txt"], key_size=2, prettify_result=lambda line: line.title())

if __name__ == '__main__':
    print(RIVER_DE.roll())
