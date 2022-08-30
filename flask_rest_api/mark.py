# from lib2to3.pgen2 import token
import email
from email import message
from lib2to3.pgen2 import token
from os import access
import secrets
from flask import Flask,jsonify,request
from datetime import datetime, timedelta
from json import decoder,encoder
import json.decoder
from flask_jwt_extended import (JWTManager,jwt_required,create_access_token,get_jwt_identity)
from flask_jwt_extended import jwt_required,create_access_token,create_refresh_token
from functools import wraps
import jwt
# from  werkzeug.security import generate_password_hash, check_password_hash
import pymongo
import json
import jwt
from jwt import PyJWT
from bson import encode, json_util, ObjectId
expires= datetime.now() + timedelta(hours=24) -timedelta(hours=5)-timedelta(minutes=30)
app= Flask(__name__)
try:
	client=pymongo.MongoClient('mongodb://localhost:27017/')
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")
app.config['JWT_SECRET_KEY']='super-secret'
jwt= JWTManager(app)

mydb = client['employee']  # database name
collection = mydb['employee_1']  # collection name
collection_1 = mydb['employee']  # collection name

@app.post('/register')
def user():
    # username= request.json['username']
    # email=request.json['email']
    # password = request.json['password']
    args= request.json
    # return args
    # if len(password)<8:
    #     return jsonify({"status":401,"error":"Password is minimun 8 character"})
    # if len(username)<3 :
    #     return jsonify({"status":401,"error":"Invalid username"})
    # if not validators.email(email):
    #     return jsonify({"status":401,"error":"Invalid email"})

    try:
        all = collection.find_one({"email":args["email"]})
        data= json.loads(json_util.dumps(all))
        # print(data)
        # return data
    #         # return "created"
        if all == None:
            collection.insert_one(args)
            return jsonify({
                "status":"200",
                "massege":"Successfully register"
            }),200
        else:
            return jsonify({
                "status":"400",
                "massege":"email already exists"

            }),400
    except:
        return jsonify({
            "massege":"invalid"
        }),400

@app.post('/login')
def login():
# #     # email=request.json['email']
# #     # password = request.json['password']
    args= request.json
    # print(args)

    try:
        
        all = collection.find_one({"email":args["email"],"password":args['password']})
        data = json.loads(json_util.dumps(all))
        # print(data)
        # return data
            # print(data)
            # return "created"
        if all ==None:
            return jsonify({
                "status":"400",
                "massege":"Email or Password invalid"
            }),400
        
        # payload={
        #         'email':data['email'],
        #         # 'exp':expires
        #     }
        access_token = create_access_token(identity= data['email'])
        # print(access_token)
        # token = jwt.encode({'email':data['email'],'exp':expires}, key = "secret", algorithm = "HS256")
        # print(token)
        return jsonify({
                "token":access_token,
                "status":200,
                "message":"Successfully login"
            }),200
    except Exception as e:
        return jsonify({
            "massege":"error"+str(e)
        }),400



@app.get("/get")
@ jwt_required()
def do_get():
   
    # return "ddshkvjdhkhsadk"
    data = collection_1.find()
    all = json.loads(json_util.dumps(data))
    if data == None:
        return jsonify({
            "data":'[]'
        }),200
    else:
        return jsonify({
            "data": all
        }),200


    # return jsonify({"message":"helo"})
    # data= collection_1.find()
    # # print(data)
    # all = json.loads(json_util.dumps(data))
    # # if all == None:
    # #     return {"message":"helo"}
    # # else:
    # #     return {"message":"created"}
    # # print(all)
    # # return {
    # #         "username": all.username,
    # #         "email":all.email,
    # #         "password":all.password
    # # }


@app.post('/post')
# @ token_required
def post():
    args= request.json
    token= request.headers['Authorization'].split(" ")[1]
    # print(token)
    # if token == None:
    #     return jsonify({"message":"token invalid"}),400
    try:
        # data=jwt.decode({token},key = "secret", algorithms = ['HS256'])
        # all = json.loads(json_util.dumps(data))
        # print(all)
        newdata= collection.find({"email":args["email"]})
        print(newdata)

        if newdata == None:
            return jsonify({"message":"unathurized token"})
        else:
                all = collection_1.insert_one(args)
                return jsonify({
                    "message":"successfully post"
                }),200
    except:
        return{"message":"hello"}
    
   
    # return args
    # try:

    # all = collection_1.find_one({"email":args["email"]})
    # # pagae = json.loads(json_util.dumps(all))
    # # print(pagae)
    # # return "created"
    # if all == None:
            # collection_1.insert_one(args)
        #     var_token= request.headers['Authorization'] # get the token from the header
        #     print(var_token)
        #     return "success"
        # else:
        #     return "already"
        # #         token = var_token.split(" ")[1]
        #         print(token)
        # try:
            # if (token == None):
            #     return("Token not found")
            #     try:
                    # var_decode = jwt.decode(token, key = "secret", algorithms = ['HS256'])
                    # print(var_decode)
    #     collection_1.insert_one(args)
    #     return jsonify({
    #             "massege":"Successfully Post"}),200
    #             # except PyJWT().ExpiredSignatureError:
    #             #             return jsonify({
    #             #             "massege":"Token expired"}),400

    #             # except  Exception as e:
    #             #     return jsonify({
    #             #     "massege":"Invalid token"}),400
    # else:
    #     return jsonify({
    #         "massege":"email already exists"
    #     }),400
    #     # except Exception as e:
    #     #     return jsonify({
    #     #         "massege":"error:"+str(e)
    #     #     })    

@app.put('/put')
# @ token_required
def put():
    args= request.json
    token= request.headers['Authorization'].split(" ")[1]
    # print(token)
    # if token == None:
    #     return jsonify({"message":"token invalid"}),400
    try:
        # data=jwt.decode({token},key = "secret", algorithms = ['HS256'])
        # all = json.loads(json_util.dumps(data))
        # print(all)
        newdata= collection.find({"email":args["email"]})
        print(newdata)

        if newdata == None:
            return jsonify({"message":"unathurized token"})
        else:
                all = collection_1.find(args)
                return jsonify({
                    "message":"successfully post"
                }),200
    except:
        return{"message":"hello"}
       



if __name__ == '__main__':
    app.run(debug=True)
    