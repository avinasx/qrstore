import http.server
import socketserver
from pathlib import Path
import os

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

with socketserver.TCPServer(("", PORT), handler_object) as httpd:
    print("Server started at localhost:" + str(PORT) + " on " + str(directory)+"/"+localFolder)
    httpd.serve_forever()
