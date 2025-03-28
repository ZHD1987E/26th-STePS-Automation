# Automation tool that extracts API data from UVENTS and translates them into the three output files
# By: ZHD1987E

## Importing the necessary libraries
import requests
import csv
import json

## Getting the API data from UVENTS
theJSON = requests.get("https://uvents.nus.edu.sg/api/event/26th-steps/moduleTracks").json()

## Opening the neccessary files
f1 = open("26th-steps-data.csv", "w", newline="", encoding = "utf-8")
csvwriter = csv.writer(f1)
f2 = open("26th-steps-projectnames.md", "w", encoding = "utf-8")
f3 = open("26th-steps-videolinks.txt", "w", encoding = "utf-8")
f4 = open("26th-steps-json.json", "w", encoding = "utf-8") # required for awards processing
awardJSONDATA = {}
csvwriter.writerow(["Track", "Project Number", "Project Name", "Video Link", "Students", "Award"])

## Processing data in JSON format
for track in theJSON:
    # Going through each 'track' (courses/modules)
    nameDCT = {}
    for person in track["students"]:
        nameDCT[person["_id"]] = person["name"]
    trackCODE = track["code"]
    trackNAME = track["name"]
    f2.write(f"# {trackCODE} {trackNAME} \n")
    for project in track["projects"]:
        # Going through each 'project' in a 'track'
        projectNAME = project["name"]
        projectVIDEOURL = project["videoLink"]
        if projectVIDEOURL:
            f3.write(f"{trackCODE}-{project['refId']}: {projectVIDEOURL}\n")
        projectMEMBERS = list(map(lambda x: nameDCT[x], project["members"]))
        projectNUMBER = project["refId"]
        f2.write(f"{trackCODE}-{projectNUMBER}: {projectNAME} \n\n")
        awardJSONDATA[f"{trackCODE}-{projectNUMBER}"] = {"name": projectNAME, "members": projectMEMBERS}
        csvwriter.writerow([trackCODE, projectNUMBER, projectNAME, projectVIDEOURL, "; ".join(projectMEMBERS), ""])

f4.write(json.dumps(awardJSONDATA))
## Closing the files
f1.close()
f2.close()
f3.close()
f4.close()
