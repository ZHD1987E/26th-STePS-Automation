import requests
import csv
theJSON = requests.get("https://uvents.nus.edu.sg/api/event/26th-steps/moduleTracks").json()
f1 = open("26th-steps-data.csv", "w", newline="")
csvwriter = csv.writer(f1)
f2 = open("26th-steps-projectnames.md", "w")
csvwriter.writerow(["Track", "Project Number", "Project Name", "Video Link", "Students", "Award"])
for track in theJSON:
    nameDCT = {}
    for person in track["students"]:
        nameDCT[person["_id"]] = person["name"]
    trackCODE = track["code"]
    trackNAME = track["name"]
    f2.write(f"# {trackCODE} {trackNAME} \n")
    for project in track["projects"]:
        projectNAME = project["name"]
        projectVIDEOURL = project["videoLink"]
        projectMEMBERS = list(map(lambda x: nameDCT[x], project["members"]))
        projectNUMBER = project["refId"]
        f2.write(f"{trackCODE}-{projectNUMBER}: {projectNAME}\n")
        csvwriter.writerow([trackCODE, projectNUMBER, projectNAME, projectVIDEOURL, ";".join(projectMEMBERS), ""])
f1.close()
f2.close()
