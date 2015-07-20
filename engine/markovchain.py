import random
import itertools


class MarkovChain(object):
    def __init__(self, key_size=3, start_marker='<', end_marker='>', backoff=False):
        if key_size < 1:
            raise ValueError("key size cannot be less than 1 element")

        self._key_size = key_size
        self._start_marker = start_marker
        self._end_marker = end_marker
        self._elements = {}
        self._keys = []
        self._lower_order_chain = \
            MarkovChain(key_size - 1, start_marker, end_marker, True) if backoff and key_size > 1 else None

    def populate(self, elements):
        if self._lower_order_chain is not None:
            self._lower_order_chain.populate(elements)

        key_size = self._key_size

        elements = list(itertools.chain([self._start_marker], elements, [self._end_marker]))

        for i in range(len(elements) - key_size):
            self.put(tuple(elements[i:i + key_size]), elements[i + key_size])

    def put(self, key, next_element, start=False):

        if not len(key) == self._key_size:
            raise ValueError("Key for this chain should contain {} elements" % self._key_size)

        if next_element is None:
            raise ValueError("Element cannot be None")

        self._elements.setdefault(key, []).append(next_element)

        if str(key).startswith(self._start_marker):
            self._keys.append(key)

    def random_key(self) -> str:
        return random.choice(self._keys)

    def next_element(self, key) -> str:
        if key in self._elements:
            return random.choice(self._elements[key])
        elif self._lower_order_chain is not None:
            return self._lower_order_chain.next_element(key)
        else:
            return self._end_marker

    def elements(self, key=None, limit=10):
        key = self.random_key() if key is None else key
        if not key.startswith(self._start_marker):
            key = self._start_marker + key

        for element in key:
            if not element == self._start_marker:
                yield element

        count = self._key_size - 1

        while self._end_marker not in key and count < limit:
            next_element = self.next_element(key)
            if not next_element == self._end_marker:
                yield next_element

            key = self.shift_key(key, next_element)
            count += 1

    @staticmethod
    def shift_key(key, next_element):
        new_key = list(key[1:])
        new_key.append(next_element)
        return tuple(new_key)
