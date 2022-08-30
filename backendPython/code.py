# import ctypes
# from dataclasses import fields
from array import array
from distutils.log import error
from genericpath import exists
from http import server
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from pickle import TRUE
from unicodedata import decimal, name
from gc import collect
from http import client
from xml.dom.minidom import Element
import pymongo
from bson import json_util, ObjectId
try:
	client=pymongo.MongoClient('mongodb://localhost:27017/')
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")


mydb = client['employee']  # database name
collection = mydb['employee']  # collection name
# information = mydb.employee
HOST = "127.0.0.1"
PORT = 8000

# employee =[{
#   "id":1,
#   "name":"abhishek"
# },
# { "id":2,
#   "name":"rakesh"
# }]
# employee=[ {
#   "name":"abhi",
#   "age":23,
#   "city":"up",
#   "phone":7753,
#   "adhar":9999
# },
# {
#   "name":"sandi",
#   "age":23,
#   "city":"mp",
#   "phone":7755,
#   "adhar":9989
# }
# ]
# print(employee)
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
      # print("get method is working")
        #defining all the headers
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        # self.wfile.write("hello world".encode())
        #prints all the keys and values of the json file
        # self.wfile.write(json.dumps(employee).encode())
        all = collection.find()
        all_data = json.loads(json_util.dumps(all))
        if len(all_data) ==0:
          self.wfile.write("[]".encode())
        # element = json.loads(json_util.dumps(all))
        # for i in element:
        for i in all_data:
          # print(i)
          # self.wfile.write(json.dumps(i).encode())
          self.wfile.write(json_util.dumps(i).encode()) #you can use that one instead to handle BSON types
        # print(all)
        # self.wfile.write(json.dumps(information.find()).encode())
        # 
        # for i in range(len(all)):
        #   print(all[i])
        


####POST method defination----->
    def do_POST(self):
      # # print(self.headers)
      # # print("post method is working")
      length = int(self.headers['Content-Length']) 
      # # reads the contents of the request
      content = self.rfile.read(length)
      temp = str(content).strip('b\'') # data come from postman as string, when the use method post
      # print(temp)
      try:
        obj = json.loads(temp) # data convert as object
        # print(obj) 
        # employee.append(obj)
        all = collection.find() 
        # print(all)
        # all_data = json_util.dumps(all)
        all_data = json.loads(json_util.dumps(all))
        # print(all_data)
        var = False
        for i in range(len(all_data)):
          if all_data[i]['id'] == obj['id']:
            var= True
            return self.error_find()
        if var== False:
          data = collection.insert_one(obj)
          self.send_response(200)
          self.send_header('Content-type','text/plain')
          self.end_headers() 
          self.wfile.write(("data successfully add").encode())
          # print(data)
          # all = collection.find()
          # print(all)
          # for i in all:
          # for i in data:
            # employee.append(i)
          # print(employee)
          # self.end_headers()
          # self.wfile.write(json.dumps(employee).encode())
            # self.wfile.write(json_util.dumps(i).encode())
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
    #   print("put method is working")
      
      length = int(self.headers['Content-Length'])
      # reads the contents of the request
      content = self.rfile.read(length)
      temp = str(content).strip('b\'') # # data come from postman as string , when the use method put
      # print(temp)
      try:
        obj = json.loads(temp)  # data convert as object id =4
        alldata = collection.find()
        var = False
        for i in alldata:
          if i['id'] == obj['id']:
            var= True
            # employee[i]= obj
            i = collection.update_one(
              {'id':obj['id']},
              {'$set':obj}
            )
            # print(employee)
            break
        if var == False:
          return self.error_function()
        self.send_response(200)
        self.send_header("Content-type","text/plain")
        self.end_headers()
        # self.wfile.write(json_util.dumps((collection.find())).encode())
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
        all = collection.find()
        # print(all)
        alldata = json.loads(json_util.dumps(all)) 
        var = False
        for i in range(len(alldata)):
          if alldata[i]['id'] == obj['id']:
            var = True
            # employee.pop(i)
            collection.delete_one({"id":obj["id"]})
            # del employee[i]
            break
        if var == False:
          return self.error_function()
        self.send_response(200)
        self.send_header("Content-type","text/plain")
        self.end_headers()
        # self.wfile.write(json_util.dumps(collection.find()).encode())
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
