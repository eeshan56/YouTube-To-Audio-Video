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
		result_streams = result.streams

		if len(result_streams) == 0:
			return "-1"

		min_index = 0
		min_filesize = result_streams[0].get_filesize()

		for i in range(1, len(result_streams)):
			if result_streams[i].extension == 'mp4':
				if min_filesize > result_streams[i].get_filesize():
					min_filesize = result_streams[i].get_filesize()
					min_index = i

		my_stream = result_streams[min_index]
		filename = result.title + '.' + my_stream.extension
		my_stream.download()
		
		return filename

	except SystemExit:
		print("Something's wrong... Why is this error occuring?")
		return "-2"

	except:
		print("Something's wrong...")
		print("Unexpected error:", sys.exc_info())
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
		result_streams = video.audiostreams

		if len(result_streams) == 0:
			return "-1"

		min_index = 0
		min_filesize = result_streams[0].get_filesize()

		for i in range(1, len(result_streams)):
			if result_streams[i].extension == 'mp3':
				if min_filesize > result_streams[i].get_filesize():
					min_filesize = result_streams[i].get_filesize()
					min_index = i

		my_stream = result_streams[min_index]
		filename = result.title + '.' + my_stream.extension
		my_stream.download()
		
		return filename
		
	except SystemExit:
		print("Something's wrong... Why is this error occuring?")
		return "-2"

	except:
		print("Something's wrong...")
		print("Unexpected error:", sys.exc_info())
		return "-1"
