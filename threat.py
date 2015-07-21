#!/usr/bin/env python3
# __author__ = 'mshmidov'
# Random generator based on 'Non-Mechanical Difficulty Levels for Monstrous Threats'
# from http://blog.trilemma.com/2014/10/non-mechanical-difficulty-levels-for.html

from engine.random_table import RandomTable

SPEED = RandomTable(
    "slow",
    "fast")

COHESION = RandomTable(
    "unorganized",
    "factional",
    "cohesive",
    "militaristic",
    "gestalts")

TERRITORIALITY = RandomTable(
    "defensive",
    "territorial",
    "vengeful",
    "predatory",
    "proactive")

PERCEPTIVENESS = RandomTable(
    "oblivious",
    "inattentive",
    "vigilant")

RANGE = RandomTable(
    "stationary",
    "site-bound",
    "territorial",
    "regional")

NUMBERS = RandomTable(
    "singular",
    "numerous",
    "hordes")

OBSCURITY = RandomTable(
    "understood",
    "unknown")

DISPOSITION = RandomTable(
    (1, 70, ""),
    (71, 80, "inaccessible"),
    (81, 90, "hidden"),
    (91, 100, "sealed"))

print(" ".join([table.roll() for table in
                [SPEED, COHESION, TERRITORIALITY, PERCEPTIVENESS, RANGE, NUMBERS, OBSCURITY, DISPOSITION]]))
