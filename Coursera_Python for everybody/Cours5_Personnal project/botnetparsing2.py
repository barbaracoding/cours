import requests
import sqlite3


conn = sqlite3.connect('botnets.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Botnets')

cur.execute('''CREATE TABLE Botnets (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, nameval TEXT UNIQUE, uuid TEXT UNIQUE, datebot TEXT, description TEXT, refs TEXT, synonyms TEXT)''')

cur.execute('DROP TABLE IF EXISTS Related')

cur.execute('''CREATE TABLE Related (from_uuid TEXT UNIQUE, dest_uuid TEXT UNIQUE, PRIMARY KEY (from_uuid, dest_uuid))''')

# Open the file
json_url = "https://raw.githubusercontent.com/MISP/misp-galaxy/master/clusters/botnet.json"
r = requests.get(json_url)

# basic parsing
data = r.json()

# items:
items = []
items = data['values']

# Print la liste des botnets du json
j = 0
botnets = []
for item in items:
    name = items[j]['value']
    j = j + 1
    botnets.append(name)

i = 0
start = 0
many = int(len(botnets))

for entry in items:
    nameval = data['values'][i]['value']
    uuid = items[i]['uuid']
    if 'date' in items[i]['meta'].keys():
        datebot = items[i]['meta']['date']
    else:
        datebot = 'N/A'
    if 'description' in items[i].keys():
        description = items[i]['description']
    else:
        description = 'N/A'
    if 'refs' in items[i]['meta'].keys():
        refs = str(items[i]['meta']['refs'])
    else:
        refs = 'N/A'
    if 'synonyms' in items[i]['meta'].keys():
            syn = str(items[i]['meta']['synonyms'])
    else:
            syn = 'N/A'

    cur.execute('SELECT id FROM Botnets WHERE id=?', (start,))
    cur.execute('''INSERT OR REPLACE INTO Botnets (id, nameval, uuid, datebot, description, refs, synonyms) VALUES (?, ?, ?, ?, ?, ?, ?)''', (start, nameval, uuid, datebot, description, refs, syn))

    # Related items[i]['related'][k]['dest-uuid']
    k = 0
    if 'related' in items[i].keys():
        dest_uuid = items[i]['related'][k]['dest-uuid']
        cur.execute('SELECT uuid FROM Botnets WHERE uuid = ? ', (uuid,))
        from_uuid = cur.fetchone()[0]
        cur.execute('''INSERT OR REPLACE INTO Related (from_uuid, dest_uuid) VALUES ( ?, ? )''',(from_uuid, dest_uuid))
        k = k + 1
    else:
        dest_uuid = 'N/A'


    conn.commit()
    start = start + 1
    i = i + 1
    many = many - 1

    print(nameval, uuid, datebot, description, refs, syn)
    print(many, ' botnets left to parse.')

cur.close()
