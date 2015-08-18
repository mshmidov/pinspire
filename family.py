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
        if male is None:
            male = random.choice([True, False])
        return Person(male, self.new_name(male), self.surnames.roll(), None, None, born=born)

    def new_name(self, male):
        return self.male_names.roll() if male else self.female_names.roll()

    def child(self, father, mother, born):
        male = random.choice([True, False])
        return Person(male, self.new_name(male), father.surname, father, mother, born=born)


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
        self.death_chance = LifeEventProbability(3).put(0, [20, 10, 5]).put(22, range(3, 101))
        self.marriage_chance = LifeEventProbability().add(range(16, 24), 20).add(range(24, 40), 5)
        self.birth_chance = LifeEventProbability().add(range(16, 25), 40).add(range(25, 30), 30).add(range(30, 40), 10)

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
    person_generator = PersonGenerator('data/omorje/surname_noble.txt',
                                       'data/omorje/name_m.txt',
                                       'data/omorje/name_f.txt')

    life = Life()

    for _ in range(50):
        life.add_person(person_generator.person(None, random.randrange(-60, -12)))
    # life.add_person(woman)

    for year in range(0, 20):
        print("year {}".format(year))

        children = set()

        for person in life.persons.copy():

            if not person.dead:

                age = year - person.born

                # check for marriage
                if person.spouse is None and life.marriage_chance.check(age):
                    spouse = life.add_person(person_generator.person(not person.male, year - 17))
                    print("{} marries {}".format(person, spouse))
                    person.marry(spouse)

                # check for birth
                if not person.male and person.spouse is not None and life.birth_chance.check(age):
                    child = person_generator.child(person.spouse, person, year)
                    children.add(child)
                    print("{} is born of {} and {}".format(child, person.spouse, person))
                    if life.death_chance.check(0):
                        children.remove(child)
                        print("{} dies at {}".format(child, 0))

                # check for death
                if life.death_chance.check(age):
                    life.kill_person(person)
                    print("{} dies at {}".format(person, age))

        for child in children:
            life.add_person(child)

        print("{} living persons".format(len([person for person in life.persons if not person.dead])))
        print("{} dead persons".format(len([person for person in life.persons if person.dead])))


if __name__ == '__main__':
    generate()
