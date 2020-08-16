import requests
from bs4 import BeautifulSoup
from pytube import YouTube

print("         ----------  Youtube Video Downloader -----------")
url = input("Enter the url of the youtube video:\n")
print("-------------")
# Scrape for the title of the video

res = requests.get(url)
soup = BeautifulSoup(res.text,"html.parser")
theElem = soup.select("meta")
for a in theElem:
    thesrc = a.get("name")
    if thesrc == "title":
        theTitle = a.get("content")
        print("Title:",theTitle)

# Download the video         

yt = YouTube(url)

# # >>> yt.thumbnail_url
# # 'https://i.ytimg.com/vi/mTOYClXhJD0/default.jpg'

# theFile.streams.get_by_itag(249).download(filename = "hello there")

# theFile.streams.get_audio_only()

#  yt.streams.filter(only_audio=True)

#<Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">

# theFile.streams.last().filesize

# yt.streams.filter(res="144p",type="video")

# Complete with audio and video

# yt.streams.filter(progressive=True).first().download(filename="new")
# yt.streams.get_by_resolution(resolution: str)
availableStreams = yt.streams.filter(progressive=True,type="video")
print("############")
theStreams = []
print("These are the available resolutions")
count = -1
for a in availableStreams:
    count = count + 1
    theStreams.append(a)
    print(theStreams[count].resolution, "and file size is " + str(round(theStreams[count].filesize / 1000000,2)) + "mb")
print("-------------")

theRes = input("Enter the resolution you want to download e.g 360p \n")

print("Downloading video...")
print("-------------")
print(availableStreams.get_by_resolution(theRes).download(filename=theTitle))
# yt.captions.get_by_language_code("en").download(title=theTitle)

# print("The available subtitle languages are:")
# for theCap in yt.captions:
#     theSoup = BeautifulSoup(str(theCap),"html.parser")
#     print(theSoup.select("caption")[0].get("lang"), "code is",theSoup.select("caption")[0].get("code"))
print("-------------")
print("Video has been downloaded.")
print("-------------")
print("Thank you for using the service")