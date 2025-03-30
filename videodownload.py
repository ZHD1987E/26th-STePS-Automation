# Automated download script for videos contained in 'videolinks.txt'
# Take note this CANNOT be run on Github as it will be flagged as bot actions.
# Run this on your local machine.
# Author: ZHD1987E

## Importing the neccessary libraries
from pytubefix import YouTube
import json
import ffmpeg
import os

## Creating error log file
errorlog = open("errorlog.md", "w")
errorlog.write(f"# Error Log\n\n")
## Downloading videos
with open("26th-steps-json.dat", "r") as f:
    data = json.load(f)
    for courseName, data in data.items():
        vLink = data["videoLink"]
        if vLink == "":
            print(f"{courseName} has no videos...")
            continue
        try:
            print(f"{courseName} has videos. Downloading...")
            # Downloading the video for the project in question
            yt = YouTube(vLink)
            vStream = yt.streams.order_by('resolution').desc().first()
            aStream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
            vStream.download(filename="temp1a.webm")
            aStream.download(filename="temp2a.webm")
            ffmpeg.output(ffmpeg.input("temp1a.webm"), ffmpeg.input("temp2a.webm"), f"videos/{courseName}.mp4").run()
            print(f"{courseName} video downloaded.")
        except:
            # Logging errors
            print(f"{courseName} video download failed. Writing to error log...")
            errorlog.write(f"[{courseName}]({vLink})\n\n")
## Cleanup of temporary files
errorlog.close()
print("Videos have been downloaded.")
try:
    os.remove("temp1a.webm")
    os.remove("temp2a.webm")
    print("Temporary files removed.")
except:
    print("Nothing needs to be removed. Temporary files were removed.")