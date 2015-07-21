import random
import sys


class Row(object):
    def __init__(self, a, b=None, v=None):

        if (a is not None) and (b is not None) and (v is not None):
            self.chance_from = a
            self.chance_to = b
            self._value = v

        elif (a is not None) and (b is not None):
            self.chance_from = a
            self.chance_to = a
            self._value = b

        elif a is not None:
            self.chance_from = None
            self.chance_to = None
            self._value = a

        else:
            raise ValueError

    @property
    def value(self):
        return self._value if type(self._value) is not RandomTable else self._value.roll()


class RandomTable(object):
    def __init__(self, *rows):

        self._rows = {}
        self._lowerChance = sys.maxsize
        self._upperChance = 0

        for row in rows:
            self.add(row)

    def add(self, row):

        if type(row) is Row:
            safe_row = row
        elif type(row) is tuple:
            safe_row = Row(*row)
        else:
            safe_row = Row(row)

        row_chance_from = safe_row.chance_from or self._upperChance + 1
        row_chance_to = safe_row.chance_to or row_chance_from

        for i in range(row_chance_from, row_chance_to + 1):
            self._rows[i] = safe_row

        self._lowerChance = min(self._lowerChance, row_chance_from)
        self._upperChance = max(self._upperChance, row_chance_to)

    def roll(self):
        index = random.randrange(self._lowerChance, self._upperChance + 1)
        row = self._rows[index]
        return row.value
