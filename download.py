import pafy
import os
import sys
import subprocess

def downloadVideo(video_url):
	try:
		good_list = ['__pycache__', 'static', 'templates', 'app.py', 'download.py', 'forms.py', 'requirements.txt', 'Procfile', '.git', 'README.md', '.profile.d', 'runtime.txt', '.heroku', 'favicon.ico']
		files = os.listdir('./')
		bad_list = []
		for i in files:
			if not i in good_list:
				bad_list.append(i)
		print(bad_list)

		for i in bad_list:
			os.remove(i)

		result = pafy.new(video_url)
		MP4FILE = result.title + ".mp4"
		best_quality_video = result.getbest()
		filename = result.title + '.' + best_quality_video.extension
		best_quality_video.download()

		if filename != MP4FILE:
			command = "ffmpeg -i '" + str(filename) + "' '" + str(MP4FILE) + "'"
			subprocess.call(command, shell = True)
			return MP4FILE
		
		return filename
	except:
		print("Something's wrong...")
		print("Unexpected error:", sys.exc_info()[0])
		return "-1"

def downloadAudio(video_url):
	try:
		good_list = ['__pycache__', 'static', 'templates', 'app.py', 'download.py', 'forms.py', 'requirements.txt', 'README.md', 'runtime.txt', '.heroku', '.profile.d', '.git', 'Procfile', 'favicon.ico']
		files = os.listdir('./')
		bad_list = []
		for i in files:
			if not i in good_list:
				bad_list.append(i)
		print(bad_list)

		for i in bad_list:
			os.remove(i)
			
		
		video = pafy.new(video_url)
		best_quality_audio = video.getbestaudio()
		MP3FILE = video.title + '.mp3'
		filename = video.title + '.' + best_quality_audio.extension
		best_quality_audio.download()

		if filename != MP3FILE:
			command = "ffmpeg -i '" + str(filename) + "' '" + str(MP3FILE) + "'"
			subprocess.call(command, shell = True)
			return MP3FILE
		
		return filename
	except:
		print("Something's wrong...")
		print("Unexpected error:", sys.exc_info())
		return "-1"

# valid = False

# while not valid:

# 	video_url = input("Enter URL of the YouTube video: ")
# 	try:
# 		youtube = pytube.YouTube(video_url)
# 		video = youtube.streams.first()
# 		valid = True
# 	except:
# 		print("Something's wrong. Please check if you've entered the correct URL.\n")

# valid = False

# while not valid:

# 	resp = input("Do you want to download the audio of this video or the entire video? (Type audio/video): ")

# 	if resp.lower() == "video":

# 		print("Video is downloading...\n\n")
# 		video.download("/home/eeshan/Downloads/")
# 		print("Video has been successfully downloaded. Check your downloads folder.")
# 		valid = True

# 	elif resp.lower() == "audio":

# 		print("Audio is downloading...\n\n")
# 		video = pafy.new(video_url)
# 		best_quality_audio = video.getbestaudio()
# 		best_quality_audio.download("/home/eeshan/Downloads/")
# 		print("Audio has been successfully downloaded. Check your downloads folder.")
# 		valid = True

# 	else:

# 		print("Please enter 'audio' or 'video'\n")