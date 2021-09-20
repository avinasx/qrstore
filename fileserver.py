import http.server
import socketserver
from pathlib import Path
import os
import socket


directory = os.getcwd()
PORT = 8800


localFolder = 'filess'
web_dir = os.path.join(os.path.dirname(__file__), localFolder)
isFile = os.path.exists(web_dir.strip())
if(not isFile):
    os.mkdir(web_dir)


os.chdir(web_dir)

# class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == '/':
#             self.path = 'index.html'
#         return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create an object of the above class
# handler_object = MyHttpRequestHandler
handler_object = http.server.SimpleHTTPRequestHandler


# my_server = socketserver.TCPServer(("", PORT), handler_object)

# # Star the server
# my_server.serve_forever()


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    # doesn't even have to be reachable
    s.connect(('10.255.255.255', 1))
    IP = s.getsockname()[0]
except Exception:
    IP = '127.0.0.1'
finally:
    s.close()
   

with socketserver.TCPServer(("", PORT), handler_object) as httpd:
    print("Server started at "+ IP +":"+ str(PORT) + " on " + str(directory)+"/"+localFolder)
    httpd.serve_forever()

