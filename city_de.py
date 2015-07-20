#!/usr/bin/env python3
__author__ = 'mshmidov'

from table.markov_table import MarkovTable

CITY_DE = MarkovTable(["seed/city_de.txt"],
                      key_size=3,
                      prettify_result=lambda line: line.title(),
                      exclude_exact_matches=True)

if __name__ == '__main__':

    result = []
    while len(result) < 10:
        city = CITY_DE.roll()
        if len(city) > 4:
            result.append(city)

    for city in result:
        print(city)
