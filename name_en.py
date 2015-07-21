#!/usr/bin/env python3

from engine.util import name_generator_by_argparse
from engine.markovchain import MarkovChain, ExcludeSourceElements, FilterByPredicate

NAME_M_EN = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 4)
NAME_M_EN.populate_from(line.casefold().strip() for line in open('seed/england/names-medieval-norman-m.txt'))
NAME_M_EN.populate_from(line.casefold().strip() for line in open('seed/england/names-medieval-norse-m.txt'))
NAME_M_EN.populate_from(line.casefold().strip() for line in open('seed/england/names-medieval-rarities-m.txt'))

NAME_F_EN = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 4)
NAME_F_EN.populate_from(line.casefold().strip() for line in open('seed/england/names-medieval-norman-f.txt'))
NAME_F_EN.populate_from(line.casefold().strip() for line in open('seed/england/names-medieval-norse-f.txt'))
NAME_F_EN.populate_from(line.casefold().strip() for line in open('seed/england/names-medieval-rarities-f.txt'))

SURNAME_EN = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 4)
SURNAME_EN.populate_from(line.casefold().strip() for line in open('seed/england/surnames-old-english.txt'))
SURNAME_EN.populate_from(line.casefold().strip() for line in open('seed/england/surnames-trade.txt'))
SURNAME_EN.populate_from(line.casefold().strip() for line in open('seed/england/surnames-byname.txt'))

if __name__ == '__main__':
    name_generator_by_argparse({'male': lambda: NAME_M_EN.sequence().title(),
                                'female': lambda: NAME_F_EN.sequence().title(),
                                'surname': lambda: SURNAME_EN.sequence().title()})
