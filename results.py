import requests
import json
import csv
from collections import defaultdict

# Proof of concept only!
# Eventually, this can be used to generate certificates on the fly.
# The only OTHER option is to manually tag on the data CSV file and then have Google Apps Script manually split the required data.
# RUN THIS MANUALLY AFTER RESULTS ARE KNOWN!

theJSON = requests.get("https://uvents.nus.edu.sg/api/event/26th-steps/vote").json()
awardsDATA = open("26th-steps-json.json", "r", encoding = "utf-8")
awardsJSON = json.load(awardsDATA)
csvDATAFILE = open("26th-steps-awardees.csv", "w", newline="", encoding = "utf-8")
csvwriter = csv.writer(csvDATAFILE)
defaultCERTORDER = ["Best Project", "Second Prize", "Third Prize"]
defaultCERTNUMBER = 3
csvwriter.writerow(["Course Names and Heads", "Project Name", "Winner Name", "Award"])
for course in theJSON:
    courseCODE = course["module"]
    awards = defaultCERTORDER
    maxAwards = defaultCERTNUMBER
    courseRESULT = list(course["result"].items())
    courseRESULT.sort(key = lambda x: x[1], reverse = True)
    courseRESULT = list(map(lambda e: f"{courseCODE}-{e[0]}", courseRESULT[:maxAwards]))
    for order in range(maxAwards):
        courseAWARDDATA = awardsJSON[courseRESULT[order]]
        winnerNAME = courseAWARDDATA["name"]
        winnerMEMBERS = courseAWARDDATA["members"]
        winnerAWARD = awards[order]
        for member in winnerMEMBERS:
            csvwriter.writerow([courseCODE, winnerNAME, member, winnerAWARD])

csvDATAFILE.close()