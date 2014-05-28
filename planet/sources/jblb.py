#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# feedoo.py
#
# Copyright © 2014 Mathieu Gaborit (matael) <mathieu@matael.org>
#
#
# Distributed under WTFPL terms
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.
#

"""

"""

from  bs4 import BeautifulSoup
import requests

SOURCE_URL = "http://jblb.net/blog/tag/haum"

def fetch():
    soup = BeautifulSoup(requests.get(SOURCE_URL).text)

    return [(
        _.find('a').text,
        _.find('a').get('href'),
        'Jérôme (jblb)'
    ) for _ in soup.findAll('h2', {'class': 'title-index'})]


