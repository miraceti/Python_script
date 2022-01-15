from pytube import YouTube

DL="D:/DL/"

# vurl = "https://www.youtube.com/watch?v=ff_0hypwIPA"
vurl = "https://www.youtube.com/watch?v=tgvrtMDzMZI"

vobj = YouTube(vurl)

stream = vobj.streams.get_highest_resolution()

stream.download(DL)