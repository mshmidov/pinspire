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


def write_sorted(names, path, filename):
    output = open(file_name(path, filename), 'w')
    for name in sorted(list(set(names))):
        output.write(name + '\n')


def file_name(path, filename):
    return "".join([path, filename, '.txt'])


def load_names(page, path, filename):
    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'lxml')

    female_header = next(header for header in soup.find_all('h3') if str(header.string).startswith('Female'))

    male_names = extract_names(female_header.find_all_previous('td'), lambda n: (not n.endswith("us")))
    female_names = extract_names(female_header.find_all_next('td'), lambda n: (not n.endswith("us")))

    write_sorted(male_names, path, filename.format('names', 'm'))
    write_sorted(female_names, path, filename.format('names', 'f'))


def load_names_from_tables(page, male_table, female_table, path, filename):
    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'lxml')

    for i, table in enumerate(soup.find_all('table')):
        if i == male_table:
            names = extract_names(table.find_all('td'), lambda n: (not n.endswith("us")))
            write_sorted(names, path, filename.format('names', 'm'))

        elif i == female_table:
            names = extract_names(table.find_all('td'), lambda n: (not n.endswith("us")))
            write_sorted(names, path, filename.format('names', 'f'))


def load_surnames(page, path, filename):
    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'lxml')

    surnames = (name.string.strip().split()[0].title() for name in soup.find_all('td') if is_not_empty(name.string))

    write_sorted(surnames, path, filename.format('surnames'))


load_names('http://tekeli.li/onomastikon/England-Medieval/Norman.html',
           '../seed/england/', '{}-medieval-norman-{}')

load_names('http://tekeli.li/onomastikon/England-Saxon/Dithematic.html',
           '../seed/england/', '{}-medieval-saxon-dithematic-{}')

load_names('http://tekeli.li/onomastikon/England-Saxon/Monothematic.html',
           '../seed/england/', '{}-medieval-saxon-monothematic-{}')

load_names('http://tekeli.li/onomastikon/England-Medieval/Norse.html',
           '../seed/england/', '{}-medieval-norse-{}')

load_names('http://tekeli.li/onomastikon/England-Medieval/Saxon.html',
           '../seed/england/', '{}-medieval-saxon-{}')

load_names('http://tekeli.li/onomastikon/England-Medieval/Rarities.html',
           '../seed/england/', '{}-medieval-rarities-{}')

load_surnames('http://tekeli.li/onomastikon/England-Surnames/Old-English.html',
              '../seed/england/', '{}-old-english')

load_surnames('http://tekeli.li/onomastikon/England-Surnames/Tradenames.html',
              '../seed/england/', '{}-trade')

load_surnames('http://tekeli.li/onomastikon/England-Surnames/Byname.html',
              '../seed/england/', '{}-byname')

load_names_from_tables('http://tekeli.li/onomastikon/Europe-Medieval/Franks.html', 0, 1,
                       '../seed/europe/', '{}-medieval-franks-{}')

load_names_from_tables('http://tekeli.li/onomastikon/Europe-Medieval/Lombards.html', 0, 1,
                       '../seed/europe/', '{}-medieval-lombards-{}')

load_names_from_tables('http://tekeli.li/onomastikon/Europe-Medieval/Goths.html', 0, 1,
                       '../seed/europe/', '{}-medieval-goths-{}')

load_names('http://tekeli.li/onomastikon/Europe-Medieval/Germany.html',
           '../seed/europe/', '{}-medieval-germany-{}')

load_names('http://tekeli.li/onomastikon/Europe-Medieval/Italy.html',
           '../seed/europe/', '{}-medieval-italy-{}')

load_names('http://tekeli.li/onomastikon/Europe-Medieval/France.html',
           '../seed/europe/', '{}-medieval-france-{}')
