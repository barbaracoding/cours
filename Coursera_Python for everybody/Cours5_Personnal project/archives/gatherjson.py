import sys
import requests
import json
import pprint
import sqlite3
import dateutil.parser as parser
from bs4 import BeautifulSoup
from dateparser import parse


# Open the file
json_url = "https://raw.githubusercontent.com/MISP/misp-galaxy/master/clusters/botnet.json"
r = requests.get(json_url)

data = r.json()

# num botnets
j = 0
botnets = []
for item in data['values']:
    name = data['values'][j]['value']
    j = j + 1
    botnets.append(name)

# basic parsing
lenjson = len(botnets)

many = int(lenjson)
i = 0

while many > 0:
    botnets = []
    for item in data['values']:
        # nameval
        nameval = data['values'][i]['value']

        # uuid
        uuid = data['values'][i]['uuid']

        # datebot
        if 'date' not in data['values'][i]['meta'].keys():
            a = True
            datebot = 'None'
        else:
            a = False
            date2 = data['values'][i]['meta']['date']
            datebot = parse(date2)

        # description
        if 'description' not in data['values'][i].keys():
            a = True
        else:
            a = False
            description = data['values'][i]['description']

        # refs
        refs = []
        if 'refs' not in data['values'][i]['meta'].keys():
            a = True
        else:
            a = False
            refs = data['values'][i]['meta']['refs']

        # synonyms
        syn = []
        if 'synonyms' not in data['values'][i]['meta'].keys():
            a = True
        else:
            a = False
            syn = data['values'][i]['meta']['synonyms']



        i = i + 1
        many = many - 1
        print(many, ' botnets left to parse.')