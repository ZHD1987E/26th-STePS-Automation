from pytubefix import YouTube
import ffmpeg
import os

testVideo = YouTube("https://www.youtube.com/watch?v=DaZK1GJVy44")
testVidStream = testVideo.streams.filter(resolution="1080p").first()
testAudStream = testVideo.streams.filter(only_audio=True).order_by('abr').desc().first()
testVidStream.download(filename="temp1a.webm")
testAudStream.download(filename="temp2a.webm")
ffmpeg.output(ffmpeg.input("temp1a.webm"), ffmpeg.input("temp2a.webm"), "videos/testVideo.mp4", y = None).run()
os.remove("temp1a.webm")
os.remove("temp2a.webm")