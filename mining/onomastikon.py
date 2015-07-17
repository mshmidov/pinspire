#!/usr/bin/env python3
import re
import requests
from bs4 import BeautifulSoup


def load_names(page, filename):
    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'lxml')

    male_header = next(header for header in soup.find_all('h3') if str(header.string).startswith('Female'))
    female_header = next(header for header in soup.find_all('h3') if str(header.string).startswith('Female'))

    male_names = (name.string.strip() for name in female_header.find_all_previous('td') if name.string is not None)
    female_names = (name.string.strip() for name in female_header.find_all_next('td') if name.string is not None)

    output_m = open(filename.format('m'), 'w')
    for name in male_names:
        if not name.isspace() and not name == '' and not name.endswith("us"):
            for part in re.findall(r"[\w]+", name):
                    output_m.write(part + '\n')

    output_f = open(filename.format('f'), 'w')
    for name in female_names:
        if not name.isspace() and not name == '' and not name.endswith("us"):
            for part in re.findall(r"[\w]+", name):
                output_f.write(part + '\n')


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