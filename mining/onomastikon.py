#!/usr/bin/env python3
import re
import itertools

import requests
from bs4 import BeautifulSoup


def is_not_empty(s):
    return s is not None and not s.isspace() and not s == ''


def extract_names(name_tags, filter_function):
    return (name.title() for name in
            (itertools.chain.from_iterable(
                re.findall(r"[\w]+", name.string) for name in name_tags
                if is_not_empty(name.string)))
            if filter_function(name))


def write_sorted(names, filename):
    output = open(filename, 'w')
    for name in sorted(list(set(names))):
        output.write(name + '\n')


def load_names(page, filename):
    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'lxml')

    female_header = next(header for header in soup.find_all('h3') if str(header.string).startswith('Female'))

    male_names = extract_names(female_header.find_all_previous('td'), lambda n: (not n.endswith("us")))
    female_names = extract_names(female_header.find_all_next('td'), lambda n: (not n.endswith("us")))

    write_sorted(male_names, filename.format('m'))
    write_sorted(female_names, filename.format('f'))


def load_names_from_tables(page, male_table, female_table, filename):
    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'lxml')

    for i, table in enumerate(soup.find_all('table')):
        if i == male_table:
            names = extract_names(table.find_all('td'), lambda n: (not n.endswith("us")))
            write_sorted(names, filename.format('m'))

        elif i == female_table:
            names = extract_names(table.find_all('td'), lambda n: (not n.endswith("us")))
            write_sorted(names, filename.format('f'))


def load_surnames(page, filename):
    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'lxml')

    surnames = (name.string.strip().split()[0].title() for name in soup.find_all('td') if is_not_empty(name.string))

    write_sorted(surnames, filename.format('surnames'))


load_names('http://tekeli.li/onomastikon/England-Medieval/Norman.html',
           '../seed/england/medieval-norman-{}.txt')

load_names('http://tekeli.li/onomastikon/England-Saxon/Dithematic.html',
           '../seed/england/medieval-saxon-dithematic-{}.txt')

load_names('http://tekeli.li/onomastikon/England-Saxon/Monothematic.html',
           '../seed/england/medieval-saxon-monothematic-{}.txt')

load_names('http://tekeli.li/onomastikon/England-Medieval/Norse.html',
           '../seed/england/medieval-norse-{}.txt')

load_names('http://tekeli.li/onomastikon/England-Medieval/Saxon.html',
           '../seed/england/medieval-saxon-{}.txt')

load_names('http://tekeli.li/onomastikon/England-Medieval/Rarities.html',
           '../seed/england/medieval-rarities-{}.txt')

load_surnames('http://tekeli.li/onomastikon/England-Surnames/Old-English.html',
              '../seed/england/old-english-{}.txt')

load_surnames('http://tekeli.li/onomastikon/England-Surnames/Tradenames.html',
              '../seed/england/trade-{}.txt')

load_surnames('http://tekeli.li/onomastikon/England-Surnames/Byname.html',
              '../seed/england/byname-{}.txt')

load_names_from_tables('http://tekeli.li/onomastikon/Europe-Medieval/Franks.html', 0, 1,
                       '../seed/europe/medieval-franks-{}.txt')
