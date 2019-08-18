import sys
import requests
import json
import pprint
import sqlite3
import dateutil.parser as parser
from bs4 import BeautifulSoup


# Open the file
json_url = "https://raw.githubusercontent.com/MISP/misp-galaxy/master/clusters/botnet.json"
r = requests.get(json_url)

# basic parsing
data = r.json()

# pp def
# pp = pprint.PrettyPrinter(indent=4)

# verification
# pprint.pprint(data)


# Print la liste des botnets du json
def print_botnets():
    i = 0
    botnets = []
    for item in data['values']:
        name = data['values'][i]['value']
        i = i + 1
        botnets.append(name)
        num = len(botnets)
    print("""
We have""", num, """botnets in how json file.""")
    print("""
Our botnets are: 
===============
""")
    pp = pprint.PrettyPrinter(width=41, compact=True)
    pp.pprint(botnets)


# print_botnets()

# print la liste des descriptions du fichier
def print_descriptions():
    i = 0
    a = False
    descriptions = list()
    for item in data['values']:
        if 'description' not in data['values'][i].keys():
            a = True
        else:
            a = False
            b = data['values'][i]['description']
            descriptions.append(b)
            pp = pprint.PrettyPrinter(width=70, compact=True, indent=5)
            pp.pprint(descriptions)
        i = i + 1


# print_descriptions()


def get_description_by_id(bot_input):
    i = 0
    for value in data['values']:
        if bot_input == data['values'][i]['value']:
            print(bot_input, ': ', """
============""")
            pprint.pprint(data['values'][i]['description'])
            break
        else:
            i = i + 1
            continue


# bot_input = input('Try a bot: ')
# get_description_by_id(bot_input)

# récupérer n'importe quel élément
# lors de l'input : proposer plusieurs choix issus d'une liste

