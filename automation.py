import requests
import csv
from pytubefix import YouTube
import os
import ffmpeg
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
        f2.write(f"{trackCODE}-{projectNUMBER}: {projectNAME} \n\n")
        csvwriter.writerow([trackCODE, projectNUMBER, projectNAME, projectVIDEOURL, "; ".join(projectMEMBERS), ""])
        if projectVIDEOURL != "":
            try:
                yt = YouTube(projectVIDEOURL) # assuming ALL project videos are YouTube links
                videoStream = yt.streams.order_by('resolution').desc().first()
                audioStream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
                videoStream.download(filename="temp1.webm")
                audioStream.download(filename="temp2.webm")
                ffmpeg.output(ffmpeg.input("temp1.webm"), ffmpeg.input("temp2.webm"), f"videos/{trackCODE}-{projectNUMBER}.mp4", y = None).run()
                os.remove("temp1.webm")
                os.remove("temp2.webm")
            except:
                pass
f1.close()
f2.close()
