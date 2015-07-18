#!/usr/bin/env python3
import re
import itertools

import requests
from bs4 import BeautifulSoup


def load_names(page, filename):
    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'lxml')

    female_header = next(header for header in soup.find_all('h3') if str(header.string).startswith('Female'))

    male_names = (name.title() for name in
                  (itertools.chain.from_iterable(
                      re.findall(r"[\w]+", name.string) for name in reversed(female_header.find_all_previous('td'))
                      if is_not_empty(name.string)))
                  if not name.endswith("us"))

    female_names = (name.title() for name in
                    (itertools.chain.from_iterable(
                        re.findall(r"[\w]+", name.string) for name in female_header.find_all_next('td')
                        if is_not_empty(name.string)))
                    if not name.endswith("us"))

    output_m = open(filename.format('m'), 'w')
    for name in sorted(list(set(male_names))):
        output_m.write(name + '\n')

    output_f = open(filename.format('f'), 'w')
    for name in sorted(list(set(female_names))):
        output_f.write(name + '\n')


def load_surnames(page, filename):
    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'lxml')

    surnames = (name.string.strip().split()[0].title() for name in soup.find_all('td') if is_not_empty(name.string))

    output = open(filename.format('surnames'), 'w')
    for name in sorted(list(set(surnames))):
        output.write(name + '\n')


def is_not_empty(s):
    return s is not None and not s.isspace() and not s == ''


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
