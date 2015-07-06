__author__ = 'mshmidov'

from engine.markovchain import MarkovChain


class MarkovTable(object):
    def __init__(self, file_name, key_size=2, terminator='%', limit=20,
                 split_line=lambda line: line.casefold().strip(),
                 prettify_result=lambda line: line.capitalize()):
        self.limit = limit
        self.prettify = prettify_result

        self.chain = MarkovChain(key_size, terminator)
        self.load_corpus(file_name, split_line)

    def load_corpus(self, file_name, line_to_elements):
        file = open(file_name)

        for line in file:
            self.chain.populate(line_to_elements(line))

    def roll(self):
        return self.prettify("".join([element for element in self.chain.elements(limit=self.limit)]))
