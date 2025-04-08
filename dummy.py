import json
import csv

# Proof of concept only!
# Eventually, this can be used to generate certificates on the fly.
# The only OTHER option is to manually tag on the data CSV file and then have Google Apps Script manually split the required data.
# RUN THIS MANUALLY AFTER RESULTS ARE KNOWN!

theMASTERDATA = open("26th-steps-awardData.dat", "r", encoding = "utf-8")
theMASTERDATAJSON = json.load(theMASTERDATA)
csvDATAFILE = open("26th-steps-awardees.csv", "w", newline="", encoding = "utf-8")
csvwriter = csv.writer(csvDATAFILE)
defaultCERTORDERRANKED = ["Best Project", "Second Prize", "Third Prize"]
defaultCERTORDERUNRANKED = "Honorable Mention"
defaultCERTNUMBER = 3
undergradSIGN = "Prof. Kan Min Yen\nVice Dean, Undergraduate Studies\nVice Dean, Academic Affairs"
gradSIGN = "Prof. Chan Mun Choon\nVice Dean, Graduate Studies"
csvwriter.writerow(["Course Names and Heads", "Project Name", "Winner Name", "Award", "Signature"])
for courseCODE, courseELEMENTS in theMASTERDATAJSON.items():

    courseNAME = courseELEMENTS["name"]
    isGraduate = courseELEMENTS["isGraduate"]
    maxAwards = courseELEMENTS["maxCerts"]
    isRanked = courseELEMENTS["ranked"]
    if isRanked:
        awards = defaultCERTORDERRANKED[:maxAwards]
    else:
        awards = [defaultCERTORDERUNRANKED] * maxAwards
    if isGraduate:
        sign = gradSIGN
    else:
        sign = undergradSIGN

    for order in range(maxAwards):
        courseAWARDDATA = awards[order]
        winnerNAME = f"{courseCODE} - "
        winnerAWARD = awards[order]
        csvwriter.writerow([courseNAME, "", winnerNAME, winnerAWARD, sign])

csvDATAFILE.close()