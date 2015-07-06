#!/usr/bin/env python3
__author__ = 'mshmidov'

from table.markov_table import MarkovTable

GERMAN_CITIES = MarkovTable("seed/german_cities.txt", key_size=3, prettify_result=lambda line: line.title())

if __name__ == '__main__':
    print(GERMAN_CITIES.roll())
