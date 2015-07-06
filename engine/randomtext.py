#!/usr/bin/env python3

from engine.markovchain import MarkovChain


class RandomText(object):
    def __init__(self, key_size=2, terminator='%'):
        self.chain = MarkovChain(key_size, terminator)

    def load_corpus(self, file_name, line_to_elements):
        file = open(file_name)

        for line in file:
            self.chain.populate(line_to_elements(line))

    def generate(self, limit=20):
        return "".join([element for element in self.chain.elements(limit=limit)])

