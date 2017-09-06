#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# fetchall.py
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

import sys
from glob import glob

OUTPUT_FILE = '../planet.rst'

HEADER = """
Planet
======

"""


def output(f_res):
    # f_res : fetch results

    with open(OUTPUT_FILE, 'w') as out:
        out.write(HEADER)

        for r in f_res:
            out.write('`' + r[0].encode('utf8') + '`__ par ' + r[2] + '\n')
            out.write('~' * (9 + len(r[0] + r[2])) + '\n\n')
            out.write('__ ' + r[1] + '\n\n')


def fetch(dirname):
    # récupère la liste des scripts source
    # et lance la fonction fetch()
    # puis met en forme

    fetch_results = []

    for i in glob(dirname+'/*.py'):
        if i != dirname + '/__init__.py':
            a = __import__(i.replace('/', '.').replace('.py', ''))
            attr = i.replace(dirname + '/', '').replace('.py', '')
            try:
                fetch_results += a.sources.__getattribute__(attr).fetch()
            except:
                e = sys.exc_info()[0]
                print('[planet] ' + attr + ' not found (are u offline ?) ' + repr(e))

    return fetch_results


def main():
    output(fetch('sources'))


if __name__ == '__main__':
    main()
