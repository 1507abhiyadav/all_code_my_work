# import ctypes
# from dataclasses import fields
import email
from lib2to3.pgen2 import token
from urllib import response
import jwt
from cryptography.hazmat.primitives import serialization
from array import array
from distutils.log import error
from genericpath import exists
from http import server
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from pickle import TRUE
from types import NoneType
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
      # self.wfile.write(("name already exist").encode())

    def error(self):
      self.send_response(404)
      self.send_header('Content-type','text/plain')
      self.end_headers()
      # self.wfile.write("id  already exist".encode())
      self.wfile.write(("name or password is invalid ").encode())
   #### login path---->
    def do_GET(self):
      if self.path == "/login":  
        length = int(self.headers['Content-Length']) 
        # # reads the contents of the request
        content = self.rfile.read(length)
        temp = str(content).strip('b\'') # data come from postman as string, when the use method post
        # print(temp)       
        try:
            obj = json.loads(temp) # data convert as object use json.loads
            # print(obj) 
            # employee.append(obj)
            # all = collection.find_one({'id':obj['id']}) # find the id in the database
            all = collection.find_one({'name':obj['name'],'password':obj['password']}) # find the name in the database
            # print(all)
            data = json.loads(json_util.dumps(all))
            # token = jwt.encode(payload = data,key = "secret")
            # print(token)
            # en_data = jwt.decode(token,key="secret", algorithms=['HS256'])
            # print(en_data)
            # print(data)
            if all == None:
                self.error()
            else:
               
              self.wfile.write(token.encode())
              self.wfile.write(json.dumps(data).encode())
              self.send_response(200)
              self.send_header('Content-type','text/json')
              self.end_headers()
                # self.wfile.write(json.dumps(en_data).encode())
        except Exception as e:
            # print(e)
            self.send_response(400)
            self.send_header('Content-type','text/plain')
            self.end_headers() 
            self.wfile.write(("error massege:"+str(e)).encode())
        except:
            self.send_response(504)
            self.send_header('Content-type','text/plain')
            self.wfile.write(("internal error"+str(e)).encode())
            # if len(all_data) ==0:
            #   self.wfile.write("[]".encode())
            # # element = json.loads(json_util.dumps(all))
            # # for i in element:
            # for i in all_data:
            #   # print(i)
            #   # self.wfile.write(json.dumps(i).encode())
            #   self.wfile.write(json_util.dumps(i).encode()) #you can use that one instead to handle BSON types


####  Sign Up method defination----->
    def do_POST(self):
      if self.path == "/register":
      # print(self.headers)
      # print("post method is working")
        length = int(self.headers['Content-Length']) 
        # # reads the contents of the request
        content = self.rfile.read(length)
        temp = str(content).strip('b\'') # data come from postman as string, when the use method post
        # print(temp)
        try:
            obj = json.loads(temp) # data convert as object use json.loads
            print(obj)
            # employee.append(obj)
            all = collection.find_one({'id':obj['id']}) # find the id in the database
            # all = collection.find_one({'name':obj['name'],'password':obj['password']}) # find the name in the database
            # print(all)
            token = jwt.encode(payload=obj,key = "secret", algorithms=['HS256'])
            print(token)
            # token = jwt.encode(payload = all,key = "secret", algorithms=['HS256'])
            # print(token) 
            if all == None:
                collection.insert_one(obj)
                self.send_response(200)
                self.send_header('Content-type','text/plain')
                self.end_headers() 
                self.wfile.write(("data successfully add").encode())
            else:
                self.error_find()
        
        except Exception as e:
            # print(e)
            self.send_response(400)
            self.send_header('Content-type','text/plain')
            self.end_headers() 
            self.wfile.write(("error massege:"+str(e)).encode())
        except:
            self.send_response(504)
            self.send_header('Content-type','text/plain')
            self.wfile.write(("internal error"+str(e)).encode())



   ####GET Method Defination----->
    def do_GET(self):
      # print("get method is working")
        #defining all the headers
        # self.send_response(200)
        # self.send_header('Content-type','text/plain')
        # self.end_headers()
        # all = collection.find()  
        length = int(self.headers['Content-Length']) 
        # # reads the contents of the request
        content = self.rfile.read(length)
        temp = str(content).strip('b\'') # data come from postman as string, when the use method post
        # print(temp)
        
        try:
            obj = json.loads(temp) # data convert as object use json.loads
            # print(obj) 
            # employee.append(obj)
            # all = collection.find_one({'id':obj['id']}) # find the id in the database
            all = collection.find_one({'name':obj['name'],'password':obj['password']}) # find the name in the database
            # print(all)
            data = json.loads(json_util.dumps(all))
            # print(data)
            if all == None:
                self.error()
            else:
              self.wfile.write(json.dumps(data).encode())
              self.send_response(200)
              self.send_header('Content-type','text/json')
              self.end_headers()
                # self.wfile.write(json.dumps(en_data).encode())
        except Exception as e:
            # print(e)
            self.send_response(400)
            self.send_header('Content-type','text/plain')
            self.end_headers() 
            self.wfile.write(("error massege:"+str(e)).encode())
        except:
            self.send_response(504)
            self.send_header('Content-type','text/plain')
            self.wfile.write(("internal error"+str(e)).encode())
            # if len(all_data) ==0:
            #   self.wfile.write("[]".encode())
            # # element = json.loads(json_util.dumps(all))
            # # for i in element:
            # for i in all_data:
            #   # print(i)
            #   # self.wfile.write(json.dumps(i).encode())
            #   self.wfile.write(json_util.dumps(i).encode()) #you can use that one instead to handle BSON types


####POST method defination----->
    def do_POST(self):
      # print(self.headers)
      # print("post method is working")
        length = int(self.headers['Content-Length']) 
        # # reads the contents of the request
        content = self.rfile.read(length)
        temp = str(content).strip('b\'') # data come from postman as string, when the use method post
        print(temp)
        
        try:
            obj = json.loads(temp) # data convert as object use json.loads
            # print(obj) 
            # employee.append(obj)
            all = collection.find_one({'id':obj['id']}) # find the id in the database
            # all = collection.find_one({'name':obj['name'],'password':obj['password']}) # find the name in the database
            # print(all)
            if all == None:
                collection.insert_one(obj)
                self.send_response(200)
                self.send_header('Content-type','text/plain')
                self.end_headers() 
                self.wfile.write(("data successfully add").encode())
            else:
                self.error_find()
        
        except Exception as e:
            # print(e)
            self.send_response(400)
            self.send_header('Content-type','text/plain')
            self.end_headers() 
            self.wfile.write(("error massege:"+str(e)).encode())
        except:
            self.send_response(504)
            self.send_header('Content-type','text/plain')
            self.wfile.write(("internal error"+str(e)).encode())

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
        data = collection.find_one({'id':obj['id']})
        if data == None:
          self.error_function()
        else:
          collection.update_one({'id':obj['id']},{'$set':obj})
          self.send_response(200)
          self.send_header('Content-type','text/plain')
          self.end_headers()
          self.wfile.write(("data successfully update").encode())

      except Exception as e:
        # print(e)
        self.send_response(400)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(("error massge:"+str(e)).encode())
      except:
        self.send_response(504)
        self.send_header('Content-type','text/plain')
        self.wfile.write(("internal error"+str(e)).encode())
        
## DELETE method defination----->

    def do_DELETE(self):
      # print("delete method is working")
      length = int(self.headers['Content-Length']) #returns the content length (value of the header) as a string. # <--- Gets the size of data

      # reads the contents of the request
      content = self.rfile.read(length) # <--- Gets the data itself
      temp = str(content).strip('b\'') # data come from postman as string , when the use method delete  
      try:
        obj = json.loads(temp)  # date convert as object 
        all = collection.find_one({'id':obj['id']})
        # print(all)
        if all == None:
          self.error_function()
        else:
          collection.delete_one({'id':obj['id']})
          self.send_response(200)
          self.send_header('Content-type','text/plain')
          self.end_headers()
          self.wfile.write(("data successfully delete").encode())
       
      except Exception as e:
        # print(e)
        self.send_response(400)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(("error  massge:"+str(e)).encode())
      except:
        self.send_response(504)
        self.send_header('Content-type','text/plain')
        self.wfile.write(("internal error"+str(e)).encode())

server= HTTPServer((HOST,PORT),ServerHTTP)
print("Server is running on port 8000")
server.serve_forever() 
