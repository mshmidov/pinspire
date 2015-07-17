#!/usr/bin/env python3

import behindthename

name_pages = ['/names/usage/english',
              '/names/usage/anglo-saxon',
              '/submit/names/usage/british']

surname_pages = ['/names/usage/english',
                 '/submit/names/usage/anglo-saxon'
                 '/submit/names/usage/english']

lang = 'en'

skip = {'Arabic', 'Ancient Greek (Latinized)', 'English (Modern)', 'Jewish', 'Biblical', 'Biblical Latin',
        'Biblical Greek', 'South African (Rare)'}

behindthename.load_names('../seed', lang, name_pages, skip)
behindthename.load_surnames('../seed', lang, surname_pages, skip)
