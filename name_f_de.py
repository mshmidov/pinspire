#!/usr/bin/env python3
__author__ = 'mshmidov'

from table.markov_table import MarkovTable

NAME_F_DE = MarkovTable(["seed/name_f_de.txt"], key_size=3, prettify_result=lambda line: line.title())

if __name__ == '__main__':
    print(NAME_F_DE.roll())
