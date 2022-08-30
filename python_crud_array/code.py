
from array import array
from http import server
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from pickle import TRUE
from unicodedata import decimal, name
from gc import collect
from http import client
from xml.dom.minidom import Element
from bson import json_util, ObjectId
HOST = "127.0.0.1"
PORT = 8000

employee =[{
  "id":1,
  "name":"abhishek"
},
{ "id":2,
  "name":"rakesh"
}]
class ServerHTTP(BaseHTTPRequestHandler):
    def _set_headers(self):
      self.send_response(200)
      self.send_header('Content-type','text/json')
      # #reads the length of the Headers
      length = int(self.headers['Content-Length'])
      # #reads the contents of the request
      content = self.rfile.read(length)
      temp = str(content).strip('b\'')
      self.end_headers()
      return temp 

    def error_function(self):
      self.send_response(404)
      self.send_header('Content-type','text/plain')
      self.end_headers()
      self.wfile.write("id not found".encode())

    def error_find(self):
      self.send_response(404)
      self.send_header('Content-type','text/plain')
      self.end_headers()
      self.wfile.write("id  already exist".encode())

   ####GET Method Defination----->
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        if len(employee) ==0:
          self.wfile.write("[]".encode())
        else:
          self.wfile.write(json.dumps(employee).encode())
            
####POST method defination----->
    def do_POST(self):
      length = int(self.headers['Content-Length']) 
      # # reads the contents of the request
      content = self.rfile.read(length)
      temp = str(content).strip('b\'') # data come from postman as string, when the use method post
      # print(temp)
      try:
        obj = json.loads(temp) # data convert as object
        var = False
        for i in range(len(employee)):
          if employee[i]['id'] == obj['id']:
            var= True
            return self.error_find()
        if var== False:
          employee.append(obj)
          self.send_response(200)
          self.send_header('Content-type','text/plain')
          self.end_headers() 
          self.wfile.write(("data successfully add").encode())
      except Exception as e:
        # print(e)
        self.send_response(400)
        self.send_header('Content-type','text/plain')
        self.end_headers() 
        self.wfile.write(("error massege:"+str(e)).encode())
      # except:
      #   self.send_response(504)
      #   self.send_header('Content-type','text/plain')
      #   self.wfile.write(("internal error"+str(e)).encode())

### PUT method defination----->

    def do_PUT(self):
      
      length = int(self.headers['Content-Length'])
      # reads the contents of the request
      content = self.rfile.read(length)
      temp = str(content).strip('b\'') # # data come from postman as string , when the use method put
      # print(temp)
      try:
        obj = json.loads(temp)  # data convert as object id =4
        var = False
        for i in range(len(employee)):
          if employee[i]['id'] == obj['id']:
            var= True
            employee[i]= obj
            break
        if var == False:
          return self.error_function()
        self.send_response(200)
        self.send_header("Content-type","text/plain")
        self.end_headers()
        self.wfile.write(("data successfully update").encode())
      except Exception as e:
        # print(e)
        self.send_response(400)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(("error massge:"+str(e)).encode())
      ## except:
      #   self.send_response(504)
      #   self.send_header('Content-type','text/plain')
      #   self.wfile.write(("internal error"+str(e)).encode())


      

        
## DELETE method defination----->

    def do_DELETE(self):
      # print("delete method is working")
      length = int(self.headers['Content-Length']) #returns the content length (value of the header) as a string. # <--- Gets the size of data

      # reads the contents of the request
      content = self.rfile.read(length) # <--- Gets the data itself
      temp = str(content).strip('b\'') # data come from postman as string , when the use method delete  
      try:
        obj = json.loads(temp)  # date convert as object 
        var = False
        for i in range(len(employee)):
          if employee[i]['id'] == obj['id']:
            var = True
            employee.pop(i)
            break
        if var == False:
          return self.error_function()
        self.send_response(200)
        self.send_header("Content-type","text/plain")
        self.end_headers()
        self.wfile.write(("data successfully delete").encode())
      except Exception as e:
        # print(e)
        self.send_response(400)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(("error  massge:"+str(e)).encode())
      ## except:
      #   self.send_response(504)
      #   self.send_header('Content-type','text/plain')
      #   self.wfile.write(("internal error"+str(e)).encode())




server= HTTPServer((HOST,PORT),ServerHTTP)
print("Server is running on port 8000")
server.serve_forever() 
