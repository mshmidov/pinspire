#!/usr/bin/env python3

from engine.util import name_generator_by_argparse
from engine.markovchain import MarkovChain, ExcludeSourceElements, FilterByPredicate

SURNAME_RU = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 3)
SURNAME_RU.populate_from(line.casefold().strip() for line in open('seed/names/russia/surnames-russian.txt'))

SURNAME_GENERAL_RU = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 3)
SURNAME_GENERAL_RU.populate_from(line.casefold().strip() for line in open('seed/names/russia/surnames-russian-general.txt'))

SURNAME_NOBLE_RU = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 5)
SURNAME_NOBLE_RU.populate_from(line.casefold().strip() for line in open('seed/names/russia/surnames-russian-noble.txt'))

SURNAME_BOYAR_RU = FilterByPredicate(ExcludeSourceElements(MarkovChain()), lambda s: len(s) > 4)
SURNAME_BOYAR_RU.populate_from(line.casefold().strip() for line in open('seed/names/russia/surnames-russian-boyar.txt'))

if __name__ == '__main__':
    name_generator_by_argparse({'simple': lambda: SURNAME_RU.sequence().title(),
                                'general': lambda: SURNAME_GENERAL_RU.sequence().title(),
                                'noble': lambda: SURNAME_NOBLE_RU.sequence().title(),
                                'boyar': lambda: SURNAME_BOYAR_RU.sequence().title()})
