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

def generate_project_list(generator):
    """ Generate a list of projects """

    projects = []
    for p in generator.pages:
        if p.source_path.find('content/pages/'+generator.settings['PROJECTS_DIR']):
            projects.append(p)

    for p in generator.pages: p.projets = projects
    return generator

class ProjectList(Directive):
    required_arguments = 0
    optional_arguments = 0
    ioption_spec = {
            'lexer': directives.unchanged,
            'encoding': directives.encoding,
            }

    def run(self):
        settings = pelican.settings.get_settings_from_file('pelicanconf.py')

        final_list = "<ul id='auto-project-list'>"
        for i in os.walk('content/pages/'+settings['PROJECTS_DIR']).next()[2]:
            with open('content/pages/'+settings['PROJECTS_DIR']+'/'+i) as f:
                parts = publish_parts(f.read(), writer_name="html4css1")

            href = settings['SITEURL']+"pages/"+slugify(parts['title'].replace('/',' '))+'.html'
            final_list +="\n<li><a href='"+href+"'>"+parts['title']+"</a></li>"

        return [nodes.raw('', final_list, format='html')]


def register():
    """ Plugin registration """
    directives.register_directive('list-projects', ProjectList)
    pelican.signals.page_generator_finalized.connect(generate_project_list)

