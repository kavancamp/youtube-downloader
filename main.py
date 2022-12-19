from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolutioon() 

  try: 
    youtubeObject.download()
  except:
    print("There has been an error in downloading your video")
  print("This download has completed!")

link = input("Enter Youtube link: ")
Download(link)
