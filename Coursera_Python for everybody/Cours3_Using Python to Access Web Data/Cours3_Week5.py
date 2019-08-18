# Extracting Data from XML

# In this assignment you will write a Python program somewhat
# similar to http://www.py4e.com/code3/geoxml.py.
# The program will prompt for a URL,
# read the XML data from that URL using urllib and then
# parse and extract
# the comment counts from the XML data, compute the sum
# of the numbers in the file.

# We provide two files for this assignment.
# One is a sample file where we give you the sum for
# your testing and the other is the actual data
# you need to process for the assignment.

# Sample data:
# http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data:
# http://py4e-data.dr-chuck.net/comments_263705.xml (Sum ends with 27)

import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
import ssl

# prompt for a URL
# address = input('Enter location: ')
address = 'http://py4e-data.dr-chuck.net/comments_42.xml'
print('Retrieving', address)

# read the XML data from that URL using urllib
url = urllib.request.urlopen(address)
data = url.read()
# test: print(data.decode())

# extract the comment counts from the XML data
tree = ET.fromstring(data)
counts = tree.findall('.//count')

liste = list()
for number in counts:
    liste.append(int(number.text))
#     print(number.text)
# test: print(type(liste[4]))

# print final:
print('Retrieved', len(data), 'characters')
print('Count:', len(liste))
print('Sum: ', sum(liste))
