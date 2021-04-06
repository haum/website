#!/usr/bin/env python
# -*- coding: utf-8 -*- #


import os
import sys

sys.path.appe
AUTHOR = u'HAUM'
SITENAME = u'Hackerspace au Mans'
SITEURL = '/'

PROJECTS_DIR = 'projets'

PATH = 'content'
STATIC_PATHS = ['images', 'calendar']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

PLUGINS = ['plugin-projets.projets', 'pelican_flickrtag']

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Calendar regeneration
from agenda.agenda import create_json
AGENDA = create_json('/home/oneshot/agenda.sqlite',
                     'content/calendar/calendar.js',
                     icalfile='content/calendar/calendar.ics')

# Custom Page generated with junja2 template for agenda
TEMPLATE_PAGES = {'agenda_template.html': 'pages/agenda.html'}

