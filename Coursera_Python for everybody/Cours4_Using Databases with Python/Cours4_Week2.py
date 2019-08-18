import sqlite3
import re

# ouverture du fichier
conn = sqlite3.connect('orgsdb.sqlite')

# création du curseur pour parcourir le fichier
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

# crée la DB sauf si elle existe déjà
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')


# read the mailbox data (mbox.txt)
# ouverture de mbox.txt
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'
fh = open(fname)

# Extraction des noms de domaines d'organisations dans listez():
listorg = list()
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    y = pieces[1].split('@')
    org = y[1]
    listorg.append(org)

# count the number of email
# messages per organization
# (i.e. domain name of the emai
# address) using a database
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

# Affichage de la DB :
# SELECT * FROM Counts ORDER BY count DESC
