#!/usr/bin/env python3
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
        if not name.isspace() and not name == '':
            output_m.write(name + '\n')

    output_f = open(filename.format('f'), 'w')
    for name in female_names:
        if not name.isspace() and not name == '':
            output_f.write(name + '\n')


load_names('http://tekeli.li/onomastikon/England-Medieval/Norman.html',
           '../seed/england/medieval-germanic-{}.txt')
