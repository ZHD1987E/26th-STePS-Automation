# Take note this CANNOT be run on Github as it will be flagged as bot actions.
# Run this on your local machine.
# Author: ZHD1987E

## Importing the neccessary libraries
import requests
import json

HEADER = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3" }

def do_download(url, filename):
    reqn = requests.get(url, headers=HEADER)
    if reqn.status_code != 200:
        raise Exception(f"Failed to download {filename}. Status code: {reqn.status_code}")
    contentType = reqn.headers.get('Content-Type')
    if not contentType or 'image' not in contentType:
        raise Exception(f"URL {url} does not point to an image. Content-Type: {contentType}")
    imgType = contentType.split('/')[-1]
    with open(f'{filename}.{imgType}', 'wb') as f:
        f.write(reqn.content)


## Creating error log file
errorlog = open("errorlog.md", "w")
errorlog.write(f"# Error Log\n\n")
## Downloading videos
with open("26th-steps-teamData.dat", "r") as f:
    data = json.load(f)
    for courseName, data in data.items():
        pLink = data["posterLink"]
        if pLink == "":
            print(f"{courseName} has no posters...")
            continue
        try:
            print(f"{courseName} has posters. Downloading...")
            # Downloading the video for the project in question
            do_download(pLink, courseName)
        except Exception as e:
            print(e)
            # Logging errors
            print(f"{courseName} poster download failed. Writing to error log...")
            errorlog.write(f"[{courseName}]({pLink})\n\n")
## Cleanup of temporary files
errorlog.close()
print("Posters have been downloaded.")