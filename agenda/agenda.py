#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# agenda.py
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

import sqlite3
import json

from datetime import date
import pelican

def events_from_query(db, q):

    db = sqlite3.connect(db)
    c = db.cursor()

    events = []
    for row in c.execute(q):
        new_event = {
                'lieu': row[0] + " - " + row[1],
                'texte': row[2]
                }

        sql_date = row[3].split(' ')
        new_event['date'] = sql_date[0].split('/') + sql_date[1].split(':')

        events.append(new_event)

    db.close()
    return events


def get_month_forall(events_list):

    for i in range(len(events_list)):
        event = events_list[i]
        py_date = date(int(event['date'][2]), int(event['date'][1]), int(event['date'][0]))
        events_list[i]['date'][1] = py_date.strftime('%b')

    return events_list


def create_json(db, calendar_file):
    """
    use the database items to generate 3 variables in the json calendar.js :
        - past_events
        - future_events
        - events = past_events + future_events

    """

    # fetch events
    past_events = events_from_query(db, "select * from agenda where status=0")
    future_events = events_from_query(db, "select * from agenda where status=1")

    # order lists
    sorted(past_events, key=lambda _: int(_['date'][2]+_['date'][1]+_['date'][0]))
    sorted(future_events, key=lambda _: int(_['date'][2]+_['date'][1]+_['date'][0]))

    past_events = get_month_forall(past_events)
    future_events = get_month_forall(future_events)

    # output
    content = """

/*** PLEASE USE SHORT MONTH NAMES ***/
var past_events = {0};
var future_events = {1};
var events = past_events + future_events;
""".format(json.dumps(past_events),json.dumps(future_events))

    with open(calendar_file, 'w') as f:

        f.write(content)

    

