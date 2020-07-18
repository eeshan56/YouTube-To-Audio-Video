# YouTube to Audio/Video:

The web app is deployed on Heroku:
http://youtube-to-audio-video.herokuapp.com/

## Installation:

### 1) Install Python3.7

The link to get the corresponding Windows or MacOS version:
https://www.python.org/downloads/release/python-377/

For Linux:
https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/

The above works for Debian distros. For other distros:
https://realpython.com/installing-python/

### 2) Create Python3.7 venv

For Linux or MacOS:
```
$ python3.7 -m venv env
$ source env/bin/activate # activate the virtual environment
```

For Windows:
```
> py -m venv env
> env\Scripts\activate # activate the virtual environment
```

### 3) Install Required Packages

```
pip install -r requirements.txt
```

## Run the server

```
python app.py
```