import random


class MarkovChain(object):
    def __init__(self, order=3, start_marker='<<<', end_marker='>>>'):
        if order < 1:
            raise ValueError("key size cannot be less than 1 element")

        self._key_size = order
        self._start_marker = start_marker
        self._end_marker = end_marker
        self._elements = {}
        self._keys = []

    def populate(self, elements: list):
        key_size = self._key_size
        elements = [self._start_marker] + list(elements) + [self._end_marker]

        for i in range(len(elements) - key_size):
            key = tuple(elements[i:i + key_size])
            next_element = elements[i + key_size]
            self._put(key, next_element)

        return self

    def generate(self, start_with: tuple=None, limit=20):
        """
        Returns an iterable for elements produced with this chain
        """
        key = random.choice(self._keys) if start_with is None else start_with
        if not key[0] == self._start_marker:
            key = self._start_marker + key

        generated = 0

        for element in key:
            if element != self._start_marker and element != self._end_marker:
                generated += 1
                yield element

        while self._end_marker not in key and generated < limit:
            next_element = self._next_element(key)
            if not next_element == self._end_marker:
                generated += 1
                yield next_element

            key = tuple(list(key[1:]) + [next_element])

    def sequence(self, start_with: tuple=None, limit=20) -> str:
        """
        Returns a string joined from elements produced with this chain
        """

        return ''.join(self.generate(start_with, limit))

    def _put(self, key: tuple, next_element):
        if not len(key) == self._key_size:
            raise ValueError("Key for this chain should contain {} elements".format(self._key_size))

        if next_element is None:
            raise ValueError("Element cannot be None")

        self._elements.setdefault(key, []).append(next_element)

        if key[0] == self._start_marker:
            self._keys.append(key)

    def _next_element(self, key: tuple) -> str:
        if key in self._elements:
            return random.choice(self._elements[key])
        else:
            print("[WARN] Chain exhausted")
            return self._end_marker


class ExcludeSourceElements(object):
    """
    Wrapper to MarkovChain.
    Ensures that generated sequence will not be equal to any of elements used to populate a chain
    """

    def __init__(self, chain: MarkovChain):
        self.chain = chain
        self.dict = set()

    def populate(self, elements: list):
        self.dict.add(elements)
        self.chain.populate(elements)

        return self

    def populate_from(self, lots_of_elements):
        for elements in lots_of_elements:
            self.dict.add(elements)
            self.chain.populate(elements)

        return self

    def generate(self, start_with: tuple=None, limit=20):
        """
           Returns an iterable for elements produced with this chain
           """
        return iter(self.sequence(start_with, limit))

    def sequence(self, start_with: tuple=None, limit=20) -> str:
        """
        Returns a string joined from elements produced with this chain
        """

        while True:
            result = ''.join(self.chain.sequence(start_with=start_with, limit=limit))
            if result not in self.dict:
                return result
