#!/usr/bin/env python3
__author__ = 'mshmidov'
import sys


from engine.markovchain import MarkovChain, ExcludeSourceElements

NAME_M_DE = ExcludeSourceElements(MarkovChain())
NAME_M_DE.populate_from(line.casefold().strip() for line in open('seed/europe/names-germanic-m.txt'))
NAME_M_DE.populate_from(line.casefold().strip() for line in open('seed/europe/names-low-german-m.txt'))
NAME_M_DE.populate_from(line.casefold().strip() for line in open('seed/europe/names-medieval-germany-m.txt'))


NAME_F_DE = ExcludeSourceElements(MarkovChain())
NAME_F_DE.populate_from(line.casefold().strip() for line in open('seed/europe/names-germanic-f.txt'))
NAME_F_DE.populate_from(line.casefold().strip() for line in open('seed/europe/names-low-german-f.txt'))
NAME_F_DE.populate_from(line.casefold().strip() for line in open('seed/europe/names-medieval-germany-f.txt'))

SURNAME_DE = ExcludeSourceElements(MarkovChain())
SURNAME_DE.populate_from(line.casefold().strip() for line in open('seed/europe/surnames-germany.txt'))


def german_name(male=True):
    name_chain = NAME_M_DE if male else NAME_F_DE

    name = [name_chain.sequence().title(), SURNAME_DE.sequence().title()]

    return " ".join(name)


if __name__ == '__main__':
    female = len(sys.argv) > 1 and sys.argv[1] == '-f'

    print(german_name(not female))
