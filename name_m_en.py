#!/usr/bin/env python3
__author__ = 'mshmidov'

from table.markov_table import MarkovTable

NAME_M_EN = MarkovTable(["seed/name_m_en.txt"],
                        key_size=3, prettify_result=lambda line: line.title(), exclude_exact_matches=True)

if __name__ == '__main__':
    print(NAME_M_EN.roll())
