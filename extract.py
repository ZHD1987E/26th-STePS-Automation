# Automation tool that extracts API data from UVENTS and translates them into the three output files
# By: ZHD1987E

## Starting the script
print("Script starting...")
## Importing the necessary libraries
import requests
import json

## Getting the API data from UVENTS
print("Downloading data from UVENTS...")
theJSON = requests.get("https://uvents.nus.edu.sg/api/event/26th-steps/moduleTracks").json()
print("Downloading done.")

## Opening the neccessary files
print("Writing files...")
f2 = open("26th-steps-projectnames.md", "w", encoding = "utf-8")
f4 = open("26th-steps-teamData.dat", "w", encoding = "utf-8") # required for awards processing
awardJSONDATA = {}
## Processing data in JSON format
for track in theJSON:
    # Going through each 'track' (courses/modules)
    nameDCT = {}
    for person in track["students"]:
        nameDCT[person["_id"]] = person["name"]
    trackCODE = track["code"]
    trackNAME = track["name"]
    f2.write(f"# {trackCODE} {trackNAME}\n")
    for project in track["projects"]:
        # Going through each 'project' in a 'track'
        projectNAME = project["name"]
        projectVIDEOURL = project["videoLink"]
        projectMEMBERS = list(map(lambda x: nameDCT[x], project["members"]))
        projectNUMBER = project["refId"]
        f2.write(f"{trackCODE}-{projectNUMBER}: {projectNAME} \n\n")
        awardJSONDATA[f"{trackCODE}-{projectNUMBER}"] = {"name": projectNAME, "members": projectMEMBERS, "videoLink": projectVIDEOURL}

f4.write(json.dumps(awardJSONDATA, indent = 4))
## Closing the files
f2.close()
f4.close()
print("Files written. Terminating script.")