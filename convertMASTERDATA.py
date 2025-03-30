import csv
import json

jOUT = {}
f1 = open('MASTERDATACSV.csv', 'r')
f2 = open('masterDATA.dat', 'w')
csvreader = csv.reader(f1)
for thing in list(csvreader):
    jOUT[thing[0]] = {"name": thing[1], "maxCerts": int(thing[2]), "isGraduate": thing[3] == "TRUE"}
f1.close()
f2.write(json.dumps(jOUT, indent=4))
f2.close()