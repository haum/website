#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

sys.path.append(os.curdir)

FLICKR_API_KEY = ''
FLICKR_API_SECRET = ''
FLICKR_USER = ''
FLICKR_TAG_CACHE_LOCATION = './tmp_flickr'
FLICKR_TAG_TEMPLATE_NAME = 'images'
FLICKR_TAG_PLACE_HOLDER_PICT = "/theme/images/haum.png"
try:
	from flickr_api.flickr_api import *
except ImportError:
	pass

AUTHOR = u'HAUM'
SITENAME = u'Hacklab au Mans'
SITEURL= '/'

PROJECTS_DIR = 'projets'

PATH = 'content'
STATIC_PATHS = ['images', 'calendar']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

PLUGINS =  ['plugin-projets.projets','pelican_flickrtag']

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
#RELATIVE_URLS = True

# planet regeneration
from planet.fetchall import fetch
PLANET = fetch('planet/sources')

# calendar regeneration
from agenda.agenda import create_json
AGENDA = create_json('/home/haum/agenda.sqlite',
                     'content/calendar/calendar.js',
                     icalfile='content/calendar/calendar.ics')

# Custom Page generated with junja2 template for agenda
TEMPLATE_PAGES = {'agenda_template.html': 'pages/agenda.html'}

