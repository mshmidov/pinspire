__author__ = 'mshmidov'

from engine.markovchain import MarkovChain


def prepare_line(line):
    return line.casefold().strip()


class MarkovTable(object):
    def __init__(self, file_names, key_size=2, limit=20,
                 split_line=prepare_line,
                 prettify_result=lambda line: line.capitalize(),
                 exclude_exact_matches=False):
        self.limit = limit
        self.prettify = prettify_result
        self.chain = MarkovChain(key_size=key_size)
        self.dict = set()
        self.exclude_exact_matches = exclude_exact_matches

        for name in file_names:
            self.load_corpus(name, split_line)

    def load_corpus(self, file_name, line_to_elements=prepare_line):
        file = open(file_name)

        for line in file:
            elements = line_to_elements(line)
            self.dict.add(elements)
            self.chain.populate(elements)

    def roll(self):
        result = self.get_from_chain()
        while self.exclude_exact_matches and result in self.dict:
            result = self.get_from_chain()

        return self.prettify(result)

    def get_from_chain(self):
        return "".join((element for element in self.chain.elements(limit=self.limit)))
