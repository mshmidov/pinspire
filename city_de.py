#!/usr/bin/env python3
__author__ = 'mshmidov'

from table.markovchain import MarkovChain, ExcludeSourceElements

CITY_DE = ExcludeSourceElements(MarkovChain())
CITY_DE.populate_from(line.casefold().strip() for line in open('seed/city_de.txt'))

if __name__ == '__main__':

    result = []
    while len(result) < 10:
        city = CITY_DE.sequence().title()
        if len(city) > 4:
            result.append(city)

    for city in result:
        print(city)
