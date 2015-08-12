#!/usr/bin/env python3
import os

import requests
from bs4 import BeautifulSoup


def clear_file(path, filename):
    if not os.path.exists(path):
        os.makedirs(path)

    with open(path + filename, 'w') as output:
        output.write('')


def load_names(page, path, filename):
    if not os.path.exists(path):
        os.makedirs(path)

    response = requests.get(page)
    response.encoding = 'cp1251'
    soup = BeautifulSoup(response.text, 'lxml')

    table = soup.find('table', width='251')
    if table is None:
        table = soup.find('table', style='width: 251px; border-collapse: collapse;')

    rows = (row.find('td') for row in table.find_all('tr'))

    with open(path + filename, 'a') as output:
        for row in rows:
            if row is not None and row.string is not None and row.string != 'фамилия':
                output.write(row.string.title() + '\n')


filepath = '../seed/names/russia/'
filename = 'surnames-russian.txt'

pages = ['http://genofond.ru/genofond.binec.ru/default2b6ad.html?p=98',
         'http://genofond.ru/genofond.binec.ru/default28bf7.html?s=0&p=100',
         'http://genofond.ru/genofond.binec.ru/default22c8b.html?s=0&p=101',
         'http://genofond.ru/genofond.binec.ru/default2f4c8.html?s=0&p=102',
         'http://genofond.ru/genofond.binec.ru/default2f2e1.html?s=0&p=69',
         'http://genofond.ru/genofond.binec.ru/default214bf.html?s=0&p=104',
         'http://genofond.ru/genofond.binec.ru/default25f36.html?s=0&p=105',
         'http://genofond.ru/genofond.binec.ru/default2e4af.html?s=0&p=106',
         'http://genofond.ru/genofond.binec.ru/default21412.html?s=0&p=107',
         'http://genofond.ru/genofond.binec.ru/default29078.html?s=0&p=108',
         'http://genofond.ru/genofond.binec.ru/default203c7.html?s=0&p=109',
         'http://genofond.ru/genofond.binec.ru/default2a0e7.html?s=0&p=110',
         'http://genofond.ru/genofond.binec.ru/default2646e.html?s=0&p=111',
         'http://genofond.ru/genofond.binec.ru/default29564.html?s=0&p=112',
         'http://genofond.ru/genofond.binec.ru/default290b8.html?s=0&p=113',
         'http://genofond.ru/genofond.binec.ru/default2b346.html?s=0&p=70',
         'http://genofond.ru/genofond.binec.ru/default2f379.html?s=0&p=115',
         'http://genofond.ru/genofond.binec.ru/default2a47f.html?s=0&p=116',
         'http://genofond.ru/genofond.binec.ru/default2eebc.html?s=0&p=117',
         'http://genofond.ru/genofond.binec.ru/default259c3.html?s=0&p=71',
         'http://genofond.ru/genofond.binec.ru/default2fcb7.html?s=0&p=119',
         'http://genofond.ru/genofond.binec.ru/default2e8fb.html?s=0&p=120',
         'http://genofond.ru/genofond.binec.ru/default2d5c5.html?s=0&p=121',
         'http://genofond.ru/genofond.binec.ru/default2e2a4.html?s=0&p=122',
         'http://genofond.ru/genofond.binec.ru/default21378.html?s=0&p=123',
         'http://genofond.ru/genofond.binec.ru/default2100c.html?s=0&p=124',
         'http://genofond.ru/genofond.binec.ru/default292e5.html?s=0&p=72',
         'http://genofond.ru/genofond.binec.ru/default29822.html?s=0&p=126',
         'http://genofond.ru/genofond.binec.ru/default2ff1b.html?s=0&p=127',
         'http://genofond.ru/genofond.binec.ru/default2fb1b.html?s=0&p=128',
         'http://genofond.ru/genofond.binec.ru/default2d422.html?s=0&p=129',
         'http://genofond.ru/genofond.binec.ru/default2dbfd.html?s=0&p=73',
         'http://genofond.ru/genofond.binec.ru/default214c0.html?s=0&p=131',
         'http://genofond.ru/genofond.binec.ru/default29c7a.html?s=0&p=74',
         'http://genofond.ru/genofond.binec.ru/default261bb.html?s=0&p=133',
         'http://genofond.ru/genofond.binec.ru/default2c62f.html?s=0&p=75',
         'http://genofond.ru/genofond.binec.ru/default243b9.html?s=0&p=233',
         'http://genofond.ru/genofond.binec.ru/default20ff8.html?s=0&p=136',
         'http://genofond.ru/genofond.binec.ru/default22c03.html?s=0&p=137',
         'http://genofond.ru/genofond.binec.ru/default22465.html?s=0&p=76',
         'http://genofond.ru/genofond.binec.ru/default2d390.html?s=0&p=139',
         'http://genofond.ru/genofond.binec.ru/default24f53.html?s=0&p=77',
         'http://genofond.ru/genofond.binec.ru/default260e1.html?s=0&p=141',
         'http://genofond.ru/genofond.binec.ru/default2fe3d.html?s=0&p=142',
         'http://genofond.ru/genofond.binec.ru/default2a970.html?s=0&p=143',
         'http://genofond.ru/genofond.binec.ru/default2febb.html?s=0&p=144',
         'http://genofond.ru/genofond.binec.ru/default2a0ef.html?s=0&p=145',
         'http://genofond.ru/genofond.binec.ru/default2d1ee.html?s=0&p=146',
         'http://genofond.ru/genofond.binec.ru/default2f043.html?s=0&p=147',
         'http://genofond.ru/genofond.binec.ru/default24735.html?s=0&p=148',
         'http://genofond.ru/genofond.binec.ru/default2696b.html?s=0&p=149',
         'http://genofond.ru/genofond.binec.ru/default23ba7.html?s=0&p=150',
         'http://genofond.ru/genofond.binec.ru/default25e33.html?s=0&p=151',
         'http://genofond.ru/genofond.binec.ru/default26e4b.html?s=0&p=152',
         'http://genofond.ru/genofond.binec.ru/default273f5.html?s=0&p=153',
         'http://genofond.ru/genofond.binec.ru/default2353c.html?s=0&p=154',
         'http://genofond.ru/genofond.binec.ru/default24021.html?s=0&p=78',
         'http://genofond.ru/genofond.binec.ru/default2bbea.html?s=0&p=156',
         'http://genofond.ru/genofond.binec.ru/default2716a.html?s=0&p=157',
         'http://genofond.ru/genofond.binec.ru/default270ab.html?s=0&p=158',
         'http://genofond.ru/genofond.binec.ru/default2bcf7.html?s=0&p=159',
         'http://genofond.ru/genofond.binec.ru/default2e471.html?s=0&p=160',
         'http://genofond.ru/genofond.binec.ru/default21cf9.html?s=0&p=79',
         'http://genofond.ru/genofond.binec.ru/default2be8d.html?s=0&p=183',
         'http://genofond.ru/genofond.binec.ru/default29b99.html?s=0&p=184',
         'http://genofond.ru/genofond.binec.ru/default24d24.html?s=0&p=185',
         'http://genofond.ru/genofond.binec.ru/default27f03.html?s=0&p=186',
         'http://genofond.ru/genofond.binec.ru/default2dbc8.html?s=0&p=187',
         'http://genofond.ru/genofond.binec.ru/default26e1c.html?s=0&p=188',
         'http://genofond.ru/genofond.binec.ru/default26075.html?s=0&p=80',
         'http://genofond.ru/genofond.binec.ru/default21a76.html?s=0&p=190',
         'http://genofond.ru/genofond.binec.ru/default2061e.html?s=0&p=81',
         'http://genofond.ru/genofond.binec.ru/default23f62.html?s=0&p=191',
         'http://genofond.ru/genofond.binec.ru/default27e6c.html?s=0&p=82',
         'http://genofond.ru/genofond.binec.ru/default272cd.html?s=0&p=193',
         'http://genofond.ru/genofond.binec.ru/default20959.html?s=0&p=194',
         'http://genofond.ru/genofond.binec.ru/default21f8b.html?s=0&p=195',
         'http://genofond.ru/genofond.binec.ru/default29c50.html?s=0&p=196',
         'http://genofond.ru/genofond.binec.ru/default27479.html?s=0&p=197',
         'http://genofond.ru/genofond.binec.ru/default2d23f.html?s=0&p=198',
         'http://genofond.ru/genofond.binec.ru/default2790c.html?s=0&p=83',
         'http://genofond.ru/genofond.binec.ru/default2432a.html?s=0&p=199',
         'http://genofond.ru/genofond.binec.ru/default21bf9.html?s=0&p=200',
         'http://genofond.ru/genofond.binec.ru/default2ddcc.html?s=0&p=84',
         'http://genofond.ru/genofond.binec.ru/default2e36d.html?s=0&p=201',
         'http://genofond.ru/genofond.binec.ru/default20c30.html?s=0&p=202',
         'http://genofond.ru/genofond.binec.ru/default287ae.html?s=0&p=203',
         'http://genofond.ru/genofond.binec.ru/default20110.html?s=0&p=204',
         'http://genofond.ru/genofond.binec.ru/default29130.html?s=0&p=205',
         'http://genofond.ru/genofond.binec.ru/default2b5c0.html?s=0&p=206',
         'http://genofond.ru/genofond.binec.ru/default2ae5e.html?s=0&p=207',
         'http://genofond.ru/genofond.binec.ru/default2dc5c.html?s=0&p=208',
         'http://genofond.ru/genofond.binec.ru/default27bab.html?s=0&p=209',
         'http://genofond.ru/genofond.binec.ru/default2f8ab.html?s=0&p=211',
         'http://genofond.ru/genofond.binec.ru/default22792.html?s=0&p=85',
         'http://genofond.ru/genofond.binec.ru/default203ed.html?s=0&p=212',
         'http://genofond.ru/genofond.binec.ru/default29924.html?s=0&p=213',
         'http://genofond.ru/genofond.binec.ru/default2155e.html?s=0&p=214',
         'http://genofond.ru/genofond.binec.ru/default27fb1.html?s=0&p=215',
         'http://genofond.ru/genofond.binec.ru/default2149e.html?s=0&p=216',
         'http://genofond.ru/genofond.binec.ru/default2acc7.html?s=0&p=88',
         'http://genofond.ru/genofond.binec.ru/default2551a.html?s=0&p=89',
         'http://genofond.ru/genofond.binec.ru/default20f00.html?s=0&p=217',
         'http://genofond.ru/genofond.binec.ru/default27b34.html?s=0&p=90',
         'http://genofond.ru/genofond.binec.ru/default2a35d.html?s=0&p=218',
         'http://genofond.ru/genofond.binec.ru/default260ec.html?s=0&p=91',
         'http://genofond.ru/genofond.binec.ru/default2652a.html?s=0&p=92',
         'http://genofond.ru/genofond.binec.ru/default233bc.html?s=0&p=231',
         'http://genofond.ru/genofond.binec.ru/default201a6.html?s=0&p=220',
         'http://genofond.ru/genofond.binec.ru/default23e19.html?s=0&p=93',
         'http://genofond.ru/genofond.binec.ru/default2d151.html?s=0&p=226',
         'http://genofond.ru/genofond.binec.ru/default2f72e.html?s=0&p=222',
         'http://genofond.ru/genofond.binec.ru/default26e4b-2.html?s=0&p=223',
         'http://genofond.ru/genofond.binec.ru/default2f01f.html?s=0&p=224',
         'http://genofond.ru/genofond.binec.ru/default20087.html?s=0&p=225',
         'http://genofond.ru/genofond.binec.ru/default2769e.html?s=0&p=94',
         'http://genofond.ru/genofond.binec.ru/default29c62.html?s=0&p=95',
         'http://genofond.ru/genofond.binec.ru/default224e0.html?s=0&p=96',
         'http://genofond.ru/genofond.binec.ru/default20298.html?s=0&p=97']

clear_file(filepath, filename)

# load_names(pages[37], filepath, filename)

for i, page in enumerate(pages):
    print(i)
    load_names(page, filepath, filename)
