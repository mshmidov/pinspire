#!/usr/bin/env python3
import os
import re
import itertools

import requests
from bs4 import BeautifulSoup


def is_not_empty(s) -> bool:
    return s is not None and not s.isspace() and not s == ''


def extract_names(name_tags, filter_function):
    return (name.title() for name in
            (itertools.chain.from_iterable(
                re.findall(r"[\w]+", name.string) for name in name_tags
                if is_not_empty(name.string)))
            if filter_function(name))


def write_sorted(names, path, filename):
    if not os.path.exists(path):
        os.makedirs(path)
    output = open(file_name(path, filename), 'w')
    for name in sorted(list(set(names))):
        output.write(name + '\n')


def file_name(path, filename):
    return "".join([path, filename, '.txt'])


def not_latin(name):
    return not name.endswith("us")


def load_names(page, path, filename):
    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'lxml')

    female_header = next(header for header in soup.find_all('h3') if str(header.string).startswith('Female'))

    male_names = extract_names(female_header.find_all_previous('td'), not_latin)
    female_names = extract_names(female_header.find_all_next('td'), not_latin)

    write_sorted(male_names, path, filename.format('names', 'm'))
    write_sorted(female_names, path, filename.format('names', 'f'))


def load_names_from_tables(page, male_table, female_table, path, filename):
    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'lxml')

    for i, table in enumerate(soup.find_all('table')):
        if i == male_table:
            names = extract_names(table.find_all('td'), not_latin)
            write_sorted(names, path, filename.format('names', 'm'))

        elif i == female_table:
            names = extract_names(table.find_all('td'), not_latin)
            write_sorted(names, path, filename.format('names', 'f'))


def load_names_from_table_first_columns(page, male_table, female_table, path, filename):
    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'lxml')

    for i, table in enumerate(soup.find_all('table')):
        if i == male_table:
            names = itertools.chain.from_iterable(
                extract_names(row.find('td'), not_latin)
                for i, row in enumerate(table.find_all('tr'))
                if i > 0)
            write_sorted(names, path, filename.format('names', 'm'))

        elif i == female_table:
            names = itertools.chain.from_iterable(
                extract_names(row.find('td'), not_latin)
                for i, row in enumerate(table.find_all('tr'))
                if i > 0)
            write_sorted(names, path, filename.format('names', 'f'))


def load_surnames(page, path, filename):
    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'lxml')

    surnames = (name.string.strip().split()[0].title() for name in soup.find_all('td') if is_not_empty(name.string))

    write_sorted(surnames, path, filename.format('surnames'))


# england

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

# medieval europe

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

# germany

load_names('http://tekeli.li/onomastikon/Europe-Western/Germany/Low-German.html',
           '../seed/europe/', '{}-low-german-{}')

load_names_from_table_first_columns('http://tekeli.li/onomastikon/Europe-Western/Germany/Germanic.html', 0, 1,
                                    '../seed/europe/', '{}-germanic-{}')

# switzerland

load_names('http://tekeli.li/onomastikon/Europe-Western/Switzerland/Firstnames.html',
           '../seed/europe/', '{}-switzerland-{}')

load_surnames('http://tekeli.li/onomastikon/Europe-Western/Switzerland/Surnames.html',
              '../seed/europe/', '{}-switzerland')

# netherlands

load_names_from_table_first_columns('http://tekeli.li/onomastikon/Europe-Western/Netherlands/Germanic.html', 0, 1,
                                    '../seed/europe/', '{}-netherlands-germanic-{}')

load_names('http://tekeli.li/onomastikon/Europe-Western/Netherlands/Friesland.html',
           '../seed/europe/', '{}-netherlands-frisian-{}')

load_surnames('http://tekeli.li/onomastikon/Europe-Western/Netherlands/Surnames.html',
              '../seed/europe/', '{}-netherlands')

# basques

load_names_from_tables('http://tekeli.li/onomastikon/Europe-Western/Basque/Male.html', 0, -1,
                       '../seed/europe/', '{}-basque-{}')

load_names_from_tables('http://tekeli.li/onomastikon/Europe-Western/Basque/Female.html', -1, 0,
                       '../seed/europe/', '{}-basque-{}')

load_surnames('http://tekeli.li/onomastikon/Europe-Western/Basque/Surnames.html',
              '../seed/europe/', '{}-basque')

# spain

load_names_from_table_first_columns('http://tekeli.li/onomastikon/Europe-Western/Spain/Germanic.html', 0, 1,
                                    '../seed/europe/', '{}-spain-germanic-{}')

load_surnames('http://tekeli.li/onomastikon/Europe-Western/Spain/Surnames.html',
              '../seed/europe/', '{}-spain')

# norway

load_names_from_table_first_columns('http://tekeli.li/onomastikon/Europe-Scandinavia/Norway/Norse.html', 0, 1,
                                    '../seed/scandinavia/', '{}-norway-norse-{}')

load_names_from_table_first_columns('http://tekeli.li/onomastikon/Europe-Scandinavia/Norway/Germanic.html', 0, 1,
                                    '../seed/scandinavia/', '{}-norway-germanic-{}')

load_surnames('http://tekeli.li/onomastikon/Europe-Scandinavia/Norway/Surnames.html',
              '../seed/scandinavia/', '{}-norway')

# sweden

load_names_from_table_first_columns('http://tekeli.li/onomastikon/Europe-Scandinavia/Sweden/Norse.html', 0, 1,
                                    '../seed/scandinavia/', '{}-sweden-norse-{}')

load_names_from_table_first_columns('http://tekeli.li/onomastikon/Europe-Scandinavia/Sweden/Germanic.html', 0, 1,
                                    '../seed/scandinavia/', '{}-sweden-germanic-{}')

load_surnames('http://tekeli.li/onomastikon/Europe-Scandinavia/Sweden/Surnames.html',
              '../seed/scandinavia/', '{}-sweden')

# denmark

load_names_from_table_first_columns('http://tekeli.li/onomastikon/Europe-Scandinavia/Denmark/Norse.html', 0, 1,
                                    '../seed/scandinavia/', '{}-denmark-norse-{}')

load_names_from_table_first_columns('http://tekeli.li/onomastikon/Europe-Scandinavia/Denmark/Germanic.html', 0, 1,
                                    '../seed/scandinavia/', '{}-denmark-germanic-{}')

load_surnames('http://tekeli.li/onomastikon/Europe-Scandinavia/Denmark/Surnames.html',
              '../seed/scandinavia/', '{}-denmark')

# faroes

load_names_from_table_first_columns('http://tekeli.li/onomastikon/Europe-Scandinavia/Faroes/Norse.html', 0, 1,
                                    '../seed/scandinavia/', '{}-faroes-norse-{}')

load_names_from_table_first_columns('http://tekeli.li/onomastikon/Europe-Scandinavia/Faroes/Norse.html', 2, 3,
                                    '../seed/scandinavia/', '{}-faroes-germanic-{}')

load_surnames('http://tekeli.li/onomastikon/Europe-Scandinavia/Faroes/Surnames.html',
              '../seed/scandinavia/', '{}-faroes')

# finland

load_names('http://tekeli.li/onomastikon/Europe-Scandinavia/Finland/Finnish.html',
           '../seed/scandinavia/', '{}-finland-finnish-{}')

load_surnames('http://tekeli.li/onomastikon/Europe-Scandinavia/Finland/Surnames.html',
              '../seed/scandinavia/', '{}-finland')
