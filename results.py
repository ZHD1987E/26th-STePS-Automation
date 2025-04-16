import requests
import json
import csv

# Proof of concept only!
# Eventually, this can be used to generate certificates on the fly.
# The only OTHER option is to manually tag on the data CSV file and then have Google Apps Script manually split the required data.
# RUN THIS MANUALLY AFTER RESULTS ARE KNOWN!

theAPIJSON = requests.get("https://uvents.nus.edu.sg/api/event/26th-steps/vote").json()
theMASTERDATA = open("26th-steps-awardData.dat", "r", encoding = "utf-8")
theMASTERDATAJSON = json.load(theMASTERDATA)
awardsDATA = open("26th-steps-teamData.dat", "r", encoding = "utf-8")
awardsJSON = json.load(awardsDATA)
csvDATAFILE = open("26th-steps-awardees.csv", "w", newline="", encoding = "utf-8")
csvwriter = csv.writer(csvDATAFILE)
theWinningTeams = open("26th-steps-winningteams.md", "w")
defaultCERTORDERRANKED = ["Best Project", "Second Prize", "Third Prize"]
defaultCERTORDERUNRANKED = "Honorable Mention"
defaultCERTNUMBER = 3
csvwriter.writerow(["Course Names and Heads", "Project Name", "Winner Name", "Award"])
for course in theAPIJSON:
    courseCODE = course["module"]

    courseNAME = theMASTERDATAJSON[courseCODE]["name"]
    isGraduate = theMASTERDATAJSON[courseCODE]["isGraduate"]
    maxAwards = theMASTERDATAJSON[courseCODE]["maxCerts"]
    isRanked = theMASTERDATAJSON[courseCODE]["ranked"]
    theWinningTeams.write(f"# {courseNAME}\n")
    if isRanked:
        awards = defaultCERTORDERRANKED[:maxAwards]
    else:
        awards = [defaultCERTORDERUNRANKED] * maxAwards
    
    courseRESULT = list(course["result"].items())
    courseRESULT.sort(key = lambda x: x[1], reverse = True)
    ranked = []
    current_group = []
    prev_score = None

    for item in courseRESULT:
        if item[1] != prev_score:
            if current_group:
                ranked.append(current_group)
            current_group = [item]
            prev_score = item[1]
        else:
            current_group.append(item)

    # Add the last group
    if current_group:
        ranked.append(current_group)
    for e in range(maxAwards):
        for winner in ranked[e]:
            projectKEY = courseCODE + "-" + winner[0]
            projectNAME = awardsJSON[projectKEY]["name"]
            theWinningTeams.write(f"**{awards[e]} ({projectKEY})** - {projectNAME}\n")
            for member in awardsJSON[projectKEY]["members"]:
                csvDATAFILE.write(f"{courseNAME}, {projectNAME}, {member}, {awards[e]}\n")

csvDATAFILE.close()
theWinningTeams.close()