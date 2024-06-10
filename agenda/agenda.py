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

import logging
import sqlite3
import json

from datetime import date, datetime
import pytz

try:
    import icalendar
except:
    logging.getLogger(__name__).warn('icalendar module not found, do not generate this part of agenda.')
    icalendar = False

def events_from_query(db, q, func=None):
    try:
        db = sqlite3.connect(db)
    except:
        logging.getLogger(__name__).warn(db + ' not found, do not generate agenda.')
        return ()
    c = db.cursor()

    if not func:
        events = []
        for row in c.execute(q):
            new_event = {
                'lieu': row[0] + " - " + row[1],
                'texte': row[2]
            }

            sql_date = row[3].split(' ')
            d = sql_date[0].split('-') + sql_date[1].split(':')
            py_date = datetime(*map(int, d))
            new_event['isodate'] = py_date.isoformat()

            events.append(new_event)

        db.close()
        return events
    else:
        return func(c.execute(q))

def ical_from_dbcursor(q):
    """
    Function to pass along with events_from_query
    """

    if not icalendar: return

    # initialize timezone
    tz = pytz.timezone('Europe/Paris')
    events = []
    for e in q:
        event = icalendar.Event()
        event.add('summary', e[0])
        event.add('description', e[2])
        event.add('location', e[1])

        sql_date = e[3].split(' ')
        d = tuple(map(int, sql_date[0].split('-') + sql_date[1].split(':')))
        date = tz.localize(datetime(d[0], d[1], d[2], d[3], d[4]))
        event.add('dtstart', date)
        events.append(event)

    return events


def create_json(db, calendar_file, icalfile=None):
    # fetch events
    now = datetime.now().replace(microsecond=0).isoformat().replace('T', ' ')[:-3]
    events = events_from_query(db, 'SELECT * FROM agenda WHERE status=1 AND date > "' + now + '" ORDER BY date ASC')

    # output
    content = "var events = {0};".format(json.dumps(events))
    with open(calendar_file, 'w') as f:
        f.write(content)

    # ICAL Generation
    if icalfile and icalendar:
        cal = icalendar.Calendar()
        sql_events = events_from_query(db, "SELECT * FROM agenda WHERE status=1 ORDER BY date DESC", ical_from_dbcursor)

        for se in sql_events:
            cal.add_component(se)

        with open(icalfile, 'wb') as f:
            f.write(cal.to_ical())
