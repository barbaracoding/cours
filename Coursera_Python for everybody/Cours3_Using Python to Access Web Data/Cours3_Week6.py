import urllib.request
import urllib.error
import json


def parsejson():
    address = input('Enter location: ')
    # address = 'http://py4e-data.dr-chuck.net/comments_263706.json'
    data = urllib.request.urlopen(address).read().decode()

    index = int(0)
    liste = []
    info = json.loads(data)

    for item in info['comments']:
        number = info['comments'][index]['count']
        # print(number)
        index = index + 1
        liste.append(number)

    print('Retrieving ', address)
    print('Retrieved', len(data), 'characters')
    print('Count:', len(liste))
    print('Sum: ', sum(liste))


parsejson()
