import json


class VirusFile:

    def __init__(self, targetfile):
        with open(targetfile, 'r') as json_file:
            self.data = json.load(json_file)

    def get_raw(self,):
        return self.data

