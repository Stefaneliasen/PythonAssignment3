import os
import urllib.request as req
import urllib.parse as urlparse
import shutil

def download(url, to=None, name=None):

    # Get data and decode
    response = req.urlopen(url).read()
    data = response.decode('UTF-8')
    path = os.getcwd()

    # If path is present get absolute path
    if(to is not None):
        path = to
    else:
    # Get relative
        path += '/download/'
    # If name is present. Make it the name of the file
    if(name is not None):
        fileName = name
    else:
    # Get last of the file
        fileName = url.split('/')[-1]
    
    file_ = open(path + fileName, 'w')
    file_.write(data)
    file_.close()
    shutil.rmtree(os.getcwd() + '/__pycache__')