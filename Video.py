#import Youtube from pytube library
from pytube import YouTube
#Youtube Video Link
link = input("Enter Youtube Link")
yt = YouTube(link)

videos = yt.streams.all()
#Select Video Format
i = 1
for stream in videos:
	print(str(i) +"__"+ str(stream))
	i += 1
stream_number = int(input("Enter Number:"))

video = videos[stream_number-1]
video.download("F:/")  #Download Directory

print("Downloaded")
