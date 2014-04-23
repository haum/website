#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# matael.py
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
Récupère depuis http://blog.matael.org/writing/tagged/haum/feed'
"""

import feedparser as fp

SOURCE_URL = 'http://blog.matael.org/writing/tagged/haum/feed'

def fetch():
    return [(_['title'], _['link'], 'Mathieu (matael)') for _ in fp.parse(SOURCE_URL)['entries']]





