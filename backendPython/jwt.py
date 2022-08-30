import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from bson import json_util, ObjectId
from requests import post
URL= "https://wv6q85jy4h.execute-api.us-east-1.amazonaws.com/employee"
employee = []
class ServerHTTP(BaseHTTPRequestHandler):
    def do_post(self):
        data= svalues
        data =json_util.dumps(data)
        return data
server= HTTPServer(URL,ServerHTTP)
# print("Server is running on port 8000")
server.serve_forever() 