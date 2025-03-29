# Automation tool that extracts API data from UVENTS and translates them into the three output files
# By: ZHD1987E

## Importing the necessary libraries
import requests
import json

## Getting the API data from UVENTS
theJSON = requests.get("https://uvents.nus.edu.sg/api/event/26th-steps/moduleTracks").json()

## Opening the neccessary files
f2 = open("26th-steps-projectnames.md", "w", encoding = "utf-8")
f3 = open("26th-steps-videolinks.dat", "w", encoding = "utf-8")
f4 = open("26th-steps-json.json", "w", encoding = "utf-8") # required for awards processing
awardJSONDATA = {}
videoLISTDATA = []
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
        if projectVIDEOURL:
            videoLISTDATA.append(f"{trackCODE}-{project['refId']}: {projectVIDEOURL}\n")
        projectMEMBERS = list(map(lambda x: nameDCT[x], project["members"]))
        projectNUMBER = project["refId"]
        f2.write(f"{trackCODE}-{projectNUMBER}: {projectNAME} \n\n")
        awardJSONDATA[f"{trackCODE}-{projectNUMBER}"] = {"name": projectNAME, "members": projectMEMBERS}

f4.write(json.dumps(awardJSONDATA))
f3.writelines(videoLISTDATA)
## Closing the files
f2.close()
f3.close()
f4.close()
