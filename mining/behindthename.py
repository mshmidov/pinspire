#!/usr/bin/env python3
import itertools

import requests
from bs4 import BeautifulSoup
import sys

from soupselect import select


def load_names(path, language, pages, skip_languages):

    site = 'http://www.behindthename.com'
    output_m = open('{}/name_{}_{}.txt'.format(path, 'm', language), 'w')
    output_f = open('{}/name_{}_{}.txt'.format(path, 'f', language), 'w')

    all_pages = itertools.chain.from_iterable([parse_navigation(site, page) for page in pages])

    for page in all_pages:

        sys.stdout.write("load_names(): {}{}\n".format(site,  page))

        response = requests.get(site + page)
        soup = BeautifulSoup(response.text, "lxml")
        items = select(soup, 'div.browsename')

        for item in items:

            # language usage
            if not any((a.string in skip_languages for a in select(item, 'a.usg'))):

                # gender usage
                male = len(select(item, 'span.masc')) > 0
                female = len(select(item, 'span.fem')) > 0

                outputs = []

                if male:
                    outputs.append(output_m)

                if female:
                    outputs.append(output_f)

                # name itself
                name_tag = select(item, 'b a')[0]
                name = name_tag.string.title() if name_tag.string is not None else name_tag.contents[0].title()
                for output in outputs:
                    output.write(name + '\n')


def load_surnames(path, language, pages, skip_languages):

    site = 'http://www.surnames.behindthename.com'
    output = open('{}/surname_{}.txt'.format(path, language), 'w')

    all_pages = itertools.chain.from_iterable([parse_navigation(site, page) for page in pages])

    for page in all_pages:

        sys.stdout.write("load_surnames(): {}{}\n".format(site,  page))

        response = requests.get(site + page)
        soup = BeautifulSoup(response.text, "lxml")
        items = select(soup, 'div.browsename')

        for item in items:

            # language usage
            if not any((a.string in skip_languages for a in select(item, 'a.usg'))):
                # name itself
                name_tag = select(item, 'b a')[0]
                name = name_tag.string.title() if name_tag.string is not None else name_tag.contents[0].title()
                output.write(name + '\n')


def parse_navigation(site, page):
    response = requests.get(site + page)
    soup = BeautifulSoup(response.text, "lxml")
    items = select(soup, 'a.sidelink')

    relations = [a.attrs['href'] for a in items] if items is not None else []
    relations.insert(0, page)

    return sorted(list(set(relations)),
                  key=lambda s: (''.join(str(s).split('/')[:-1]) + str(s).split('/')[-1].zfill(2)))
