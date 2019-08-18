from main import VirusFile
import pprint

targetfile = input('Quel Fichier ?--> ', )
file = VirusFile(targetfile)
pprint.pprint(file.get_raw())
#print(file.get_structure())

