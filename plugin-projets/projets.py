#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# projets.py
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

import pelican

from docutils.parsers.rst import directives, Directive
from docutils.core import publish_parts
from docutils import nodes

from pelican.utils import slugify

import os
import re


def generate_banners_jsonindex(generator):
    listing = {}
    script = "projectalea_list = Array('"
    for _, _, i in os.walk('/content/images/bannieres_projets'):
        for _file in i:
            sp = _file.split('.')
            if len(sp) == 3 and sp[2] == 'jpg':
                listing[sp[0]] = sp[1]
    script += "', '".join(listing)
    script += "');\n"
    script += "projectalea_sublist = Array(Array('"
    script += "'), Array('".join((", ".join(listing[n1]) for n1 in listing))
    script += "'));"
    script += """
projectalea_ind = Math.floor(Math.random() * projectalea_list.length)
projectalea_chosen = projectalea_list[projectalea_ind];
projectalea_subchosen = projectalea_sublist[projectalea_ind][Math.floor(Math.random() * projectalea_sublist[projectalea_ind].length)];
document.write('<p><a href="/pages/' + projectalea_chosen + '.html"><img src="/images/bannieres_projets/' + projectalea_chosen + '.' + projectalea_subchosen + '.jpg"/></a></p>');"""
    dirname = 'content/images/bannieres_projets/'
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(dirname + "projectalea.js", "w") as f:
        f.write(script)


def generate_project_list(generator):
    """ Generate a list of projects """

    projects = []

    for p in generator.pages:
        path = 'content/pages/'+generator.settings['PROJECTS_DIR']
        if p.source_path.find(path) > 0:
            projects.append(p)

    for p in generator.pages:
        p.projets = projects

    return generator


def ordered_walk(path):
    return sorted(os.walk(path).next()[2])

class ProjectList(Directive):
    required_arguments = 0
    optional_arguments = 0

    ioption_spec = {
        'lexer': directives.unchanged,
        'encoding': directives.encoding,
    }

    def run(self):
        settings = pelican.settings.get_settings_from_file('pelicanconf.py')

        proj_dir = 'content/pages/' + settings['PROJECTS_DIR']

        final_list = "<ul id='auto-project-list'>"

        for i in ordered_walk(proj_dir):

            ignored = False

            # Ignore folders, temporary files
            for j in (r'^\.', r'\.swp$', r'~$'):
                if re.match(j, i):
                    ignored = True
                    break
            if ignored:
                continue

            with open('content/pages/'+settings['PROJECTS_DIR']+'/'+i) as f:
                parts = publish_parts(f.read(), writer_name="html4css1")

            with open('content/pages/'+settings['PROJECTS_DIR']+'/'+i) as f:
                l = ''
                slug = ''
                while not re.match(r'^:slug:', l):
                    try:
                        l = f.readline()
                    except IOError:
                        print('End of file, no slug found, '
                              'using title instead')
                        slug = slugify(parts['title'])
                        break

                if not slug:
                    slug = re.sub(r':slug:(.*)', r'\1', l)
                    slug = slug.strip()

            href = settings['SITEURL'] + "pages/" + slug + '.html'
            final_list += "\n<li><a href='" + href + "'>" + parts['title'] \
                + "</a></li>"

        return [nodes.raw('', final_list, format='html')]


def register():
    """ Plugin registration """
    directives.register_directive('list-projects', ProjectList)
    pelican.signals.page_generator_finalized.connect(generate_project_list)
    pelican.signals.static_generator_init.connect(generate_banners_jsonindex)
