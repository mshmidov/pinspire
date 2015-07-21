#!/usr/bin/env python3

__author__ = 'mshmidov'
import sys

from engine.markovchain import MarkovChain, ExcludeSourceElements

NAME_M_EN = ExcludeSourceElements(MarkovChain())
NAME_M_EN.populate_from(line.casefold().strip() for line in open('seed/england/names-medieval-norman-m.txt'))
NAME_M_EN.populate_from(line.casefold().strip() for line in open('seed/england/names-medieval-norse-m.txt'))
NAME_M_EN.populate_from(line.casefold().strip() for line in open('seed/england/names-medieval-rarities-m.txt'))

NAME_F_EN = ExcludeSourceElements(MarkovChain())
NAME_F_EN.populate_from(line.casefold().strip() for line in open('seed/england/names-medieval-norman-f.txt'))
NAME_F_EN.populate_from(line.casefold().strip() for line in open('seed/england/names-medieval-norse-f.txt'))
NAME_F_EN.populate_from(line.casefold().strip() for line in open('seed/england/names-medieval-rarities-f.txt'))

SURNAME_EN = ExcludeSourceElements(MarkovChain())
SURNAME_EN.populate_from(line.casefold().strip() for line in open('seed/england/surnames-old-english.txt'))
SURNAME_EN.populate_from(line.casefold().strip() for line in open('seed/england/surnames-trade.txt'))
SURNAME_EN.populate_from(line.casefold().strip() for line in open('seed/england/surnames-byname.txt'))


def english_name(male=True):
    name_chain = NAME_M_EN if male else NAME_F_EN

    name = [name_chain.sequence().title(), SURNAME_EN.sequence().title()]

    return " ".join(name)


if __name__ == '__main__':
    female = len(sys.argv) > 1 and sys.argv[1] == '-f'

    print(english_name(not female))
