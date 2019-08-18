# 10.2 Write a program to read through the
# mbox-short.txt and figure out the distribution
# by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line
# by finding the time and then splitting the string
# a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.'''

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name, 'r')
list2 = list()
list3 = list()
counts = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        line = (line.rstrip()).split(" ")
        list2.append(line[6])
for time in list2:
    time = time.split(":")
    list3.append(time[0])

for hour in list3:
    counts[hour] = counts.get(hour, 0) + 1
# print(counts)

tmp = list()
for h, n in counts.items():
    tmp.append((h, n))
    tmp = sorted(tmp)
# print(tmp)

for h, n in tmp:
    print(h, n)

# line = (line.rstrip()).split(" ")
# print(line[1])
# print(list3)
# counts[word] = counts.get(word,0) +1
