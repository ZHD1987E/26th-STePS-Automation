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
undergradSIGN = "Prof. Kan Min Yen\nVice Dean, Undergraduate Studies\nVice Dean, Academic Affairs"
gradSIGN = "Prof. Chan Mun Choon\nVice Dean, Graduate Studies"
csvwriter.writerow(["Course Names and Heads", "Project Name", "Winner Name", "Award", "Signature"])
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
    if isGraduate:
        sign = gradSIGN
    else:
        sign = undergradSIGN
    
    courseRESULT = list(course["result"].items())
    courseRESULT.sort(key = lambda x: x[1], reverse = True)
    courseRESULT = list(map(lambda e: f"{courseCODE}-{e[0]}", courseRESULT[:maxAwards]))

    for order in range(maxAwards):
        projectCODE = courseRESULT[order]
        courseAWARDDATA = awardsJSON[projectCODE]
        winnerNAME = courseAWARDDATA["name"]
        winnerMEMBERS = courseAWARDDATA["members"]
        winnerAWARD = awards[order]
        theWinningTeams.write(f"**{winnerAWARD} ({projectCODE})** - {winnerNAME}\n\n")
        for member in winnerMEMBERS:
            csvwriter.writerow([courseNAME, winnerNAME, member, winnerAWARD, sign])

csvDATAFILE.close()
theWinningTeams.close()