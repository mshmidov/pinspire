#!/usr/bin/env python3
import random

from random_table import RandomTable


class Person(object):
    def __init__(self, male, name, surname, father, mother, born=0, spouse=None):
        self.male = male
        self.name = name
        self.surname = surname
        self.born = born
        self.father = father
        self.mother = mother
        self.children = set()
        if spouse is None:
            self.spouse = None
        else:
            self.marry(spouse)
        self.dead = False

    def __str__(self):
        return "({}) {} [{}]".format('m' if self.male else 'f', self.name, self.surname)

    def marry(self, other):
        self.spouse = other
        if other.spouse is None:
            other.marry(self)
        if not self.male:
            self.surname = other.surname

    def distance(self, other):
        if self.mother is None or self.father is None or other.mother is None or other.father is None:
            return 0
        elif self.mother is other.mother or self.father is other.father:
            return 1
        else:
            return min(self.father.distance(other.father), self.mother.distance(other.mother),
                       self.father.distance(other.mother), self.mother.distance(other.father)) + 1


class PersonGenerator(object):
    def __init__(self, surnames, male_names, female_names):
        self.surnames = RandomTable(*[line.strip().title() for line in open(surnames)])
        self.male_names = RandomTable(*[line.strip().title() for line in open(male_names)])
        self.female_names = RandomTable(*[line.strip().title() for line in open(female_names)])

    def person(self, male, born=-17):
        return Person(male, self.new_name(male), self.surnames.roll(), None, None, born=born)

    def new_name(self, male):
        return self.male_names.roll() if male else self.female_names.roll()

    def child(self, father, mother, born):
        male = random.choice([True, False])
        return Person(True, self.new_name(male), father.surname, father, mother, born=born)


class LifeEventProbability(object):
    def __init__(self, default=0):
        self.probability = [default for _ in range(120)]

    def add(self, age, chance):
        try:
            for i in age:
                self.probability[i] = chance
        except TypeError:
            self.probability[age] = chance

        return self

    def put(self, age, chances):
        for i, chance in enumerate(chances):
            self.probability[age + i] = chance

        return self

    def check(self, age):
        chance = self.probability[age]
        return chance > 0 and random.randrange(1, 101) < chance


class Life(object):
    def __init__(self):
        self.persons = set()
        self.death_chance = LifeEventProbability(5).put(0, [30, 20, 15, 10]).put(24, range(5, 101))
        self.marriage_chance = LifeEventProbability().add(range(16, 24), 20).add(range(24, 40), 5)

    def add_person(self, person: Person):
        self.persons.add(person)
        return person

    def kill_person(self, person: Person):
        if person.spouse is not None:
            person.spouse.spouse = None
            person.spouse = None
        person.dead = True
        return person


def generate():
    person_generator = PersonGenerator('data/omorje/surname_noble.txt', 'data/omorje/name_m.txt',
                                       'data/omorje/name_f.txt')

    life = Life()
    man = person_generator.person(True)
    # woman = person_generator.person(False)
    # man.marry(woman)

    life.add_person(man)
    # life.add_person(woman)

    for year in range(0, 300):
        print("year {}".format(year))

        for person in life.persons.copy():
            if not person.dead:

                age = year - person.born
                # check for marriage
                if person.spouse is None and life.marriage_chance.check(age):
                    spouse = life.add_person(person_generator.person(not person.male, year - 17))
                    person.marry(spouse)
                    print("{} marries {}".format(person, spouse))

                # check for birth

                # check for death
                if life.death_chance.check(age):
                    life.kill_person(person)
                    print("{} dies at {}".format(person, age))


if __name__ == '__main__':
    generate()
