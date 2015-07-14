#!/usr/bin/env python3
__author__ = 'mshmidov'

from table.markov_table import MarkovTable

CITY_DE = MarkovTable(["seed/city_de.txt"], key_size=3, prettify_result=lambda line: line.title())

if __name__ == '__main__':
    print(CITY_DE.roll())
