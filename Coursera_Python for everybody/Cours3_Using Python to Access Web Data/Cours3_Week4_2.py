# urllinks-like

# Following Links in Python

# In this assignment you will write a Python program that expands
# on http://www.py4e.com/code3/urllinks.py.
# The program will use urllib to read the HTML from the data files
# below, extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position relative to
# the first name in the list, follow that link and repeat the
# process a number of times and report the last name you find.

# We provide two files for this assignment. One is a sample file
# where we give you the name for your testing and the other is
# the actual data you need to process for the assignment

# Sample problem:
# Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1).
# Follow that link. Repeat this process 4 times.
# The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah

# Actual problem:
# Start at: http://py4e-data.dr-chuck.net/known_by_Aelish.html
# Find the link at position 18 (the first name is 1).
# Follow that link. Repeat this process 7 times.
# The answer is the last name that you retrieve.

# Hint: The first character of the name of the last page
# that you will load is: R

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import urlopen
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# inputs
# count = 0
# position = 0

count = None
position = None
url = input('Enter - ')
count = input('Enter count: ')
count = int(count)
if count <= 0:
    print("LOOSER")
    quit()
position = input('Enter position: ')
position = int(position) - 1
if position < 0:
    quit()

# parsing bs4
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

print("Retrieving: ", url)

# Retrieve all of the anchor tags
tags = soup('a')
y = list()
for tag in tags:
    y.append(tag.get('href', None))
print("Retrieving: ", y[position])
count = count - 1

while count is not 0:
    # ouverture du second lien
    new_url = y[position]
    html = urlopen(new_url, context=ctx).read()
    # parsing bs4
    soup = BeautifulSoup(html, "html.parser")
    # Retrieve all of the anchor tags
    tags = soup('a')
    y = list()
    for tag in tags:
        y.append(tag.get('href', None))
    print("Retrieving: ", y[position])
    count = count - 1


'''
y.append(print(tag.get('href', None)))

while position is 0:
    try:
    except:
        print('Pease enter a number: ')
        continue
'''

# print(y)
# for tag in soup.find_all("a"):
#     print("{0}: {1}".format(tag.name, tag.text))


#   y.append(int(tag.contents[0]))
#     print(" ".join(tag.text.split()))

# y.append(tag.get('href', None))
# y.append(tag.contents[0])
# print(y)

# Retrieve the corresponding tags

'''tags = soup('span')
for tag in tags:
    y = (y.split())'''

# Look at the parts of a tag
# print('TAG:', tag)
# print('URL:', tag.get('href', None))'''
