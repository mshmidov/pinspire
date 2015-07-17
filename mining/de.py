#!/usr/bin/env python3

import behindthename

name_pages = ['/names/usage/german',
              '/names/usage/ancient-germanic'
              '/submit/names/usage/german',
              '/submit/names/usage/german-east-prussian',
              '/submit/names/usage/german-silesian']

surname_pages = ['/names/usage/german',
                 '/submit/names/usage/ancient-germanic',
                 '/submit/names/usage/german',
                 '/submit/names/usage/german-east-prussian',
                 '/submit/names/usage/german-silesian']

lang = 'de'

skip = {'Arabic', 'Ancient Greek (Latinized)', 'English (Modern)', 'Jewish', 'Biblical', 'Biblical Latin',
        'Biblical Greek', 'Jewish'}

behindthename.load_names('../seed', lang, name_pages, skip)
behindthename.load_surnames('../seed', lang, surname_pages, skip)
