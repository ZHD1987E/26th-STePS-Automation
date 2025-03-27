from pytubefix import YouTube
import ffmpeg
import os
with open("26th-steps-videolinks.txt", "r") as f:
    data = f.read().split("\n")
    for entry in data:
        entry = entry.split(": ")
        yt = YouTube(entry[1])
        vStream = yt.streams.order_by('resolution').desc().first()
        aStream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        vStream.download(filename="temp1a.webm")
        aStream.download(filename="temp2a.webm")
        ffmpeg.output(ffmpeg.input("temp1a.webm"), ffmpeg.input("temp2a.webm"), f"videos/{entry[0]}.mp4", y = None).run()
# cleanup after all videos downloaded, instead of deleting after each video
os.remove("temp1a.webm")
os.remove("temp2a.webm")