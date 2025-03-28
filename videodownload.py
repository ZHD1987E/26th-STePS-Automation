# Automated download script for videos contained in 'videolinks.txt'
# Take note this CANNOT be run on Github as it will be flagged as bot actions.
# Run this on your local machine.
# Author: ZHD1987E

## Importing the neccessary libraries
from pytubefix import YouTube
import ffmpeg
import os

## Creating error log file
errorlog = open("errorlog.md", "w")
errorlog.write(f"# Error Log\n\n")
## Downloading videos
with open("26th-steps-videolinks.dat", "r") as f:
    data = f.read().split("\n")
    for entry in data:
        entry = entry.split(": ")
        try:
            # Downloading the video for the project in question
            yt = YouTube(entry[1])
            vStream = yt.streams.order_by('resolution').desc().first()
            aStream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
            vStream.download(filename="temp1a.webm")
            aStream.download(filename="temp2a.webm")
            ffmpeg.output(ffmpeg.input("temp1a.webm"), ffmpeg.input("temp2a.webm"), f"videos/{entry[0]}.mp4").run()
        except:
            # Logging errors
            errorlog.write(f"[{entry[0]}]({entry[1]})\n\n")
## Cleanup of temporary files
errorlog.close()
os.remove("temp1a.webm")
os.remove("temp2a.webm")