import requests
import json
import csv

# Proof of concept only!

# Eventually, this can be used to generate certificates on the fly.
# The only OTHER option is to manually tag on the data CSV file and then have Google Apps Script manually split the required data.
theJSON = requests.get("https://uvents.nus.edu.sg/api/event/26th-steps/vote").json()
awardsDATA = open("26th-steps-json.json", "r", encoding = "utf-8")
awardsJSON = json.load(awardsDATA)
csvDATAFILE = open("26th-steps-awardees.csv", "w", newline="", encoding = "utf-8")
csvwriter = csv.writer(csvDATAFILE)
csvwriter.writerow(["Track", "Project Number", "Project Name", "Students", "Award"])
awardDESC = {0: "Best Project Award", 1: "1st Runners Up", 2: "2nd Runners Up"} # Will be adjusted if need be
print(awardsJSON)
for course in theJSON:
    courseCODE = course["module"]
    courseRESULT = list(course["result"].items())
    courseRESULT.sort(key = lambda x: x[1], reverse = True)
    courseRESULT = list(map(lambda e: f"{courseCODE}-{e[0]}", courseRESULT[:3])) # Top 3, this CANNOT be adjusted
    for order in range(3):
        courseAWARDDATA = awardsJSON[courseRESULT[order]]
        courseNAME = courseAWARDDATA["name"]
        courseMEMBERS = courseAWARDDATA["members"]
        for member in courseMEMBERS:
            csvwriter.writerow([courseCODE, courseRESULT[order].split("-")[1], courseNAME, member, awardDESC[order]])

csvDATAFILE.close()