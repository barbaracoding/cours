import urllib.request
import urllib.error
import xml.etree.ElementTree as ET


def parsexml():
    address = input('Enter location: ')
    data = urllib.request.urlopen(address).read()
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    liste = list()
    for number in counts:
        liste.append(int(number.text))
    print('Retrieved', len(data), 'characters')
    print('Count:', len(liste))
    print('Sum: ', sum(liste))


parsexml()
