#!/usr/bin/env python3

from engine.markovchain import MarkovChain, ExcludeSourceElements, FilterByPredicate
from engine.util import name_generator_by_argparse

NAME_M_DE = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 4)
NAME_M_DE.populate_from(line.casefold().strip() for line in open('seed/names/europe/names-germanic-m.txt'))
NAME_M_DE.populate_from(line.casefold().strip() for line in open('seed/names/europe/names-low-german-m.txt'))
NAME_M_DE.populate_from(line.casefold().strip() for line in open('seed/names/europe/names-medieval-germany-m.txt'))

NAME_F_DE = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 4)
NAME_F_DE.populate_from(line.casefold().strip() for line in open('seed/names/europe/names-germanic-f.txt'))
NAME_F_DE.populate_from(line.casefold().strip() for line in open('seed/names/europe/names-low-german-f.txt'))
NAME_F_DE.populate_from(line.casefold().strip() for line in open('seed/names/europe/names-medieval-germany-f.txt'))

SURNAME_DE = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 4)
SURNAME_DE.populate_from(line.casefold().strip() for line in open('seed/names/europe/surnames-germany.txt'))

if __name__ == '__main__':
    name_generator_by_argparse({'male': lambda: NAME_M_DE.sequence().title(),
                                'female': lambda: NAME_F_DE.sequence().title(),
                                'surname': lambda: SURNAME_DE.sequence().title()})
