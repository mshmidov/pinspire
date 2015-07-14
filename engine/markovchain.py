import random
import itertools


class MarkovChain(object):
    def __init__(self, key_size=3, terminator=None, backoff=False):
        if key_size < 1:
            raise ValueError("key size cannot be less than 1 element")

        self._key_size = key_size
        self._terminator = terminator
        self._elements = {}
        self._keys = []
        self._lower_order_chain = MarkovChain(key_size - 1, terminator) if backoff and key_size > 2 else None

    @property
    def terminator(self):
        return self._terminator

    @property
    def terminated(self):
        return self._terminator is not None

    @property
    def key_size(self):
        return self._key_size

    def populate(self, elements):
        if self._lower_order_chain is not None:
            self._lower_order_chain.populate(elements)

        key_size = self.key_size

        elements = list(itertools.chain(elements, list(self.terminator))) if self.terminated else elements

        for n, i in enumerate(range(len(elements) - key_size)):
            self.put(tuple(elements[i:i + key_size]), elements[i + key_size], n == 0)

    def put(self, key, next_element, start=False):

        if not len(key) == self._key_size:
            raise ValueError("Key for this chain should contain {} elements" % self._key_size)

        if self.terminator in key:
            raise ValueError("Key cannot contain terminator symbol '{}'" % self.terminator)

        if next_element is None:
            raise ValueError("Element cannot be None")

        self._elements.setdefault(key, []).append(next_element)

        if start:
            self._keys.append(key)

    def random_key(self):
        return random.choice(self._keys)

    def next_element(self, key):
        if key in self._elements:
            return random.choice(self._elements[key])
        elif self._lower_order_chain is not None:
            return self._lower_order_chain.next_element(key)
        else:
            return self._terminator

    def elements(self, key=None, limit=10):

        key = self.random_key() if key is None else key

        for element in key:
            yield element

        count = self._key_size
        while self.terminator not in key and count < limit:
            next_element = self.next_element(key)
            if not next_element == self.terminator:
                yield next_element

            key = self.shift_key(key, next_element)
            count += 1

    @staticmethod
    def shift_key(key, next_element):
        new_key = list(key[1:])
        new_key.append(next_element)
        return tuple(new_key)
