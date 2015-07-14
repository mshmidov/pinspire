#!/usr/bin/env python3
import random
import sys

__author__ = 'mshmidov'

from table.markov_table import MarkovTable

NAME_M_DE = MarkovTable(["seed/name_m_de.txt", "seed/name_m_de_prussian.txt", "seed/name_m_de_silesian.txt"],
                        key_size=3, prettify_result=lambda line: line.title(), exclude_exact_matches=True)

NAME_F_DE = MarkovTable(["seed/name_f_de.txt", "seed/name_f_de_prussian.txt", "seed/name_f_de_silesian.txt"],
                        key_size=3, prettify_result=lambda line: line.title(), exclude_exact_matches=True)

SURNAME_DE = MarkovTable(["seed/surname_de.txt", "seed/surname_de_prussian.txt", "seed/surname_de_silesian.txt"],
                         key_size=3, prettify_result=lambda line: line.title(), exclude_exact_matches=True)


def german_name(male=True):
    name_chain = NAME_M_DE if male else NAME_F_DE

    name = []

    for i in range(random.randint(1, 3)):
        name.append(name_chain.roll())

    name.append(SURNAME_DE.roll())

    return " ".join(name)


if __name__ == '__main__':
    female = len(sys.argv) > 1 and sys.argv[1] == '-f'

    print(german_name(not female))
