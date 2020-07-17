
from flask import Flask, render_template, redirect, request, url_for, flash, send_file
from werkzeug.utils import secure_filename
from forms import MainForm, FormatChoices


from download import downloadVideo, downloadAudio

import pafy
import os

host = '0.0.0.0'

app = Flask(__name__)
app.secret_key = '0f728c6b5c9f6e02690f9496da4818ae'

def verify(url):
    """
	To check whether `url` belongs to YouTube, if yes returns True
	else False
	"""
    if "www.youtube.com" in url or "youtu.be" in url:
        return True
    return False

@app.route("/", methods = ['GET', 'POST'])
@app.route("/home", methods = ['GET', 'POST'])
def home():
	form = MainForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			if not verify(form.url_field.data):
				flash('Please enter a valid URL', 'danger')

			format_display = dict(FormatChoices).get(form.output_format.data)

			if format_display == 'Video':
				result = downloadVideo(form.url_field.data)
				print(result)
				if result == "-1":
					flash('Please enter a valid URL', 'danger')
				else:
					flash('File successfully converted', 'success')
					form.url_field.data = ""
					return redirect('/downloadfile/' + result)

			elif format_display == "Audio":
				result = downloadAudio(form.url_field.data)

				if result == "-1":
					flash('Please enter a valid URL', 'danger')
				else:
					flash('File successfully converted', 'success')
					return redirect('/downloadfile/' + result)
			
	return render_template('index.html', form = form)

@app.route('/render_video', defaults = {'URL' : ''})
def render_video(URL):

	return render_template('render_video.html', URL = URL, width = width, height = height)

@app.route('/downloadfile/<filename>', methods = ['GET'])
def download_file(filename):
	return render_template('download.html', value = filename, title = 'Download')

@app.route('/return-files/<filename>')
def return_files_tut(filename):
	file_path = ""
	if '/' in filename:
		file_path = filename.split('/')[-1]
	elif '\\' in filename:
		file_path = filename.split('/')[-1]
	else:
		file_path = filename

	# file_path = filename
	return send_file(file_path, as_attachment = True, attachment_filename = '')

@app.route("/about")
def about():
	return render_template('about.html')

if __name__ == '__main__':
	#logged_in = False
	app.run(host = host, debug = True)