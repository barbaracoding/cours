import sqlite3
import time
import zlib
import string

conn = sqlite3.connect('botnets.sqlite')
cur = conn.cursor()

cur.execute('SELECT id, description FROM Botnets')
Botnets = dict()
for line in cur :
    Botnets[line[0]] = line[1]

cur.execute('SELECT id FROM Botnets')
counts = dict()
for line in cur :
    text = Botnets[line[0]]
    text = text.translate(str.maketrans('','',string.punctuation))
    text = text.translate(str.maketrans('','','1234567890'))
    text = text.strip()
    text = text.lower()
    words = text.split()
    for word in words:
        if len(word) < 4 : continue
        counts[word] = counts.get(word,0) + 1

x = sorted(counts, key=counts.get, reverse=True)
highest = None
lowest = None
for k in x[:100]:
    if highest is None or highest < counts[k] :
        highest = counts[k]
    if lowest is None or lowest > counts[k] :
        lowest = counts[k]
print('Range of counts:',highest,lowest)

# Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20

fhand = open('botword.js','w')
fhand.write("botword = [")
first = True
for k in x[:100]:
    if not first : fhand.write( ",\n")
    first = False
    size = counts[k]
    size = (size - lowest) / float(highest - lowest)
    size = int((size * bigsize) + smallsize)
    fhand.write("{text: '"+k+"', size: "+str(size)+"}")
fhand.write( "\n];\n")
fhand.close()

print("Output written to botword.js")
print("Open botword.htm in a browser to see the vizualization")
