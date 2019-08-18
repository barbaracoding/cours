import sys
import requests
import json
import pprint
import sqlite3
import ssl
import dateutil.parser as parser
from bs4 import BeautifulSoup
from dateparser import parse

conn = sqlite3.connect('botnets.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Botnets')

cur.execute('''CREATE TABLE Botnets (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE , nameval TEXT UNIQUE, uuid TEXT UNIQUE, datebot TEXT, description TEXT, refs TEXT, synonyms TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Related (from_uuid TEXT UNIQUE, dest_uuid TEXT UNIQUE)''')


# Open the file
json_url = "https://raw.githubusercontent.com/MISP/misp-galaxy/master/clusters/botnet.json"
r = requests.get(json_url)

# basic parsing
data = r.json()

# Print la liste des botnets du json
j = 0
botnets = []
for item in data['values']:
    name = data['values'][j]['value']
    j = j + 1
    botnets.append(name)

# Check to see if we are already in progress...
'''
cur.execute('SELECT id,refs FROM Botnets WHERE description is NULL and nameval is NULL ORDER BY RANDOM() LIMIT 1')
row = cur.fetchone()
if row is not None:
    print("Restarting existing crawl.  Remove botnets.sqlite to start a fresh crawl.")

else:
    if len(data) > 1:
        sys.exit()
'''

start = 0
lenjson = len(botnets)
many = int(lenjson)
i = 0

while many > 0:
    start = start + 1
    cur.execute('SELECT id FROM Botnets WHERE id=?', (start,))
    try:
        row = cur.fetchone()
        if row is not None:
            continue
    except:
        row = None

    botnets = []
    for item in data['values']:
        # nameval
        nameval = data['values'][i]['value']

        cur.execute('''INSERT OR IGNORE INTO Botnets (nameval)
            VALUES ( ? )''', (nameval,))

        # uuid
        uuid = data['values'][i]['uuid']

        cur.execute('''INSERT OR IGNORE INTO Botnets (uuid)
            VALUES ( ? )''', (uuid,))

        # datebot
        if 'date' not in data['values'][i]['meta'].keys():
            a = True
            datebot = 'None'
        else:
            a = False
            date2 = data['values'][i]['meta']['date']
            datebot = date2

            cur.execute('''INSERT OR IGNORE INTO Botnets (datebot)
            VALUES ( ? )''', (datebot,))

        # description
        if 'description' not in data['values'][i].keys():
            a = True
        else:
            a = False
            description = data['values'][i]['description']

            cur.execute('''INSERT OR IGNORE INTO Botnets (description)
            VALUES ( ? )''', (description,))

        # refs
        refs = []
        if 'refs' not in data['values'][i]['meta'].keys():
            a = True
        else:
            a = False
            refs = data['values'][i]['meta']['refs']
            refs = str(refs)
            cur.execute('''INSERT OR IGNORE INTO Botnets (refs) VALUES ( ? )''', (refs, ))

        # synonyms
        syn = []
        if 'synonyms' not in data['values'][i]['meta'].keys():
            a = True
        else:
            a = False
            syn = data['values'][i]['meta']['synonyms']
            syn = str(syn)

            cur.execute('''INSERT OR IGNORE INTO Botnets (synonyms)
            VALUES ( ? )''', (syn,))

        i = i + 1
        many = many - 1
        conn.commit()
        print(nameval, uuid, datebot, description, refs, syn)
        print(many, ' botnets left to parse.')

cur.close()

        # cur.execute('INSERT OR IGNORE INTO Botnets (nameval, uuid, datebot, description, refs, synonyms) VALUES (?, ?, ?, ?, ?, ?)', (nameval, uuid, datebot, description, refs, syn))






