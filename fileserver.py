from pathlib import Path
import os
import socket
from flask import Flask, request, jsonify, render_template, send_from_directory
import qrcode
from PIL import Image


#get IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(('10.255.255.255', 1))
    IP = s.getsockname()[0]
except Exception:
    IP = '127.0.0.1'
finally:
    s.close()
   

directory = os.getcwd() #get current
PORT = 8000 #change this to desired port
# lsof -ti:8000 | xargs kill 
localFolder = 'FILES' #change this to desired directory
localFolderDownloads = 'Downloads/QRCODES' #change this to desired directory


web_dir = os.path.join(os.path.dirname(__file__), localFolder) #append localdir to localfolder
# web_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', localFolder))


isFile = os.path.exists(web_dir.strip()) #stip the path and check if it exists

# make directory if not exists
if(not isFile):
    os.mkdir(web_dir)

#get tree
def make_tree(path):
    tree = dict(name=os.path.basename(path), children=[])
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                tree['children'].append(dict(name=name))
    return tree

app = Flask(__name__, static_url_path='', static_folder=localFolder)

@app.route('/')
def dirtree():
    # path = os.path.expanduser(web_dir)
    return render_template('index.html', tree=make_tree(web_dir), web_dir = web_dir)


@app.route('/custom/js/<path:filename>')
def custom_static_js(filename):
    return send_from_directory(app.root_path + '/custom/js/', filename)


@app.route('/custom/css/<path:filename>')
def custom_static_css(filename):
    return send_from_directory(app.root_path + '/custom/css/', filename)



@app.route('/gen', methods=[ 'POST']) 
def gen():
    print(request) 
    link = request.json["link"]
    fname = request.json["fname"]
    imgQr = qrcode.make(link)
    downloads_path = str(Path.home() / localFolderDownloads)

    isFile = os.path.exists(downloads_path.strip()) #stip the path and check if it exists
    # make directory if not exists
    if(not isFile):
        os.mkdir(downloads_path)
    
    imgQr.save(downloads_path+'/'+fname+"_QR.jpg")
    print('saving')
    return {"success" :"true"}


if(IP):
    if __name__=="__main__":
        app.run(host=IP, port=PORT, debug=True)
else:
   if __name__=="__main__":
    app.run(host="localhost", port=PORT, debug=True) 


