#!/usr/bin/env python3
"""
Exporte agenda.sqlite (alimenté par le bot hms_agenda) vers data/agenda.json.
Hugo génère ensuite la page agenda, les prochains évènements de l'accueil
et le fichier iCal (/calendar/calendar.ics) — plus besoin de icalendar/pytz.

Usage : python tools/agenda_export.py ../website/agenda.sqlite data/agenda.json
"""

import json
import os
import sqlite3
import sys


def main(db_path, out_path):
    db = sqlite3.connect(db_path)
    rows = db.execute(
        'SELECT titre, lieu, description, date FROM agenda '
        'WHERE status=1 ORDER BY date ASC')
    events = [{'titre': t, 'lieu': l, 'description': (d or '').strip(),
               'date': date.replace(' ', 'T') + ':00'}
              for t, l, d, date in rows]
    os.makedirs(os.path.dirname(out_path) or '.', exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(events, f, ensure_ascii=False, indent=2)
    print(f'{len(events)} évènements exportés')


if __name__ == '__main__':
    main(*sys.argv[1:3])
