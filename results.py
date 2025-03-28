import requests
import json
import csv
from collections import defaultdict

# Proof of concept only!
# Eventually, this can be used to generate certificates on the fly.
# The only OTHER option is to manually tag on the data CSV file and then have Google Apps Script manually split the required data.
# RUN THIS MANUALLY AFTER RESULTS ARE KNOWN!
# This applies to Undergraudate category only.

theAPIJSON = requests.get("https://uvents.nus.edu.sg/api/event/26th-steps/vote").json()
theMASTERDATA = open("masterDATA.json", "r", encoding = "utf-8")
theMASTERDATAJSON = json.load(theMASTERDATA)
awardsDATA = open("26th-steps-json.json", "r", encoding = "utf-8")
awardsJSON = json.load(awardsDATA)
csvDATAFILE = open("26th-steps-awardees.csv", "w", newline="", encoding = "utf-8")
csvwriter = csv.writer(csvDATAFILE)
defaultCERTORDERUNDERGRAD = ["Best Project", "Second Prize", "Third Prize"]
defaultCERTORDERGRAD = "Honorable Mention"
defaultCERTNUMBER = 3
csvwriter.writerow(["Course Names and Heads", "Project Name", "Winner Name", "Award"])
for course in theAPIJSON:
    courseCODE = course["module"]

    courseNAME = theMASTERDATAJSON[courseCODE]["name"]
    isGraduate = theMASTERDATAJSON[courseCODE]["isGraduate"]
    maxAwards = theMASTERDATAJSON[courseCODE]["maxAwards"]

    if isGraduate:
        awards = [defaultCERTORDERGRAD] * maxAwards
    else:
        awards = defaultCERTORDERUNDERGRAD
    
    courseRESULT = list(course["result"].items())
    courseRESULT.sort(key = lambda x: x[1], reverse = True)
    courseRESULT = list(map(lambda e: f"{courseCODE}-{e[0]}", courseRESULT[:maxAwards]))

    for order in range(maxAwards):
        courseAWARDDATA = awardsJSON[courseRESULT[order]]
        winnerNAME = courseAWARDDATA["name"]
        winnerMEMBERS = courseAWARDDATA["members"]
        winnerAWARD = awards[order]
        
        for member in winnerMEMBERS:
            csvwriter.writerow([courseNAME, winnerNAME, member, winnerAWARD])

csvDATAFILE.close()