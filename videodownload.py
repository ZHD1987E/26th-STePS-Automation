# Automated download script for videos contained in 'videolinks.txt'
# Take note this CANNOT be run on Github as it will be flagged as bot actions.
# Run this on your local machine.
# Author: ZHD1987E

## Importing the neccessary libraries
import yt_dlp
import json

def do_download(url, filename):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'videos/{filename}.mp4',  # Custom filename
        'merge_output_format': 'mp4'   # Ensure MP4 output
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

## Creating error log file
errorlog = open("errorlog.md", "w")
errorlog.write(f"# Error Log\n\n")
## Downloading videos
with open("26th-steps-teamData.dat", "r") as f:
    data = json.load(f)
    for courseName, data in data.items():
        vLink = data["videoLink"]
        if vLink == "":
            print(f"{courseName} has no videos...")
            continue
        try:
            print(f"{courseName} has videos. Downloading...")
            # Downloading the video for the project in question
            do_download(vLink, courseName)
        except:
            # Logging errors
            print(f"{courseName} video download failed. Writing to error log...")
            errorlog.write(f"[{courseName}]({vLink})\n\n")
## Cleanup of temporary files
errorlog.close()
print("Videos have been downloaded.")