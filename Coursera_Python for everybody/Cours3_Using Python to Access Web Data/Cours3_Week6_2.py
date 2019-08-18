import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

address = input('Enter location: ')

parms = dict()

parms['address'] = address

parms['key'] = api_key

url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)

uh = urllib.request.urlopen(url)

data = uh.read().decode()

print('Retrieved', len(data), 'characters')

js = json.loads(data)

# print(data)

print('Place id', js['results'][0]['place_id'])
