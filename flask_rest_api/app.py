import email
import json
# from typing_extensions import Required
import jwt
# from flask_jwt import JWT, jwt_required, current_identity
# from wsgiref import headers
# from json import decoder
# import json.decoder
from flask import Flask,jsonify,request
# import validators
from datetime import datetime, timedelta
from bson import encode, json_util, ObjectId
from pymongo import MongoClient
import pymongo
expires= datetime.now() + timedelta(hours=24) -timedelta(hours=5)-timedelta(minutes=30)
app= Flask(__name__)
try:
	client=pymongo.MongoClient('mongodb://localhost:27017/')
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")

mydb = client['employee']  # database name
collection = mydb['employee_1']  # collection name
collection_1 = mydb['employee_2']  # collection name

@app.post('/register')
def user():
    # username= request.json['username']
    # email=request.json['email']
    # password = request.json['password']
    args= request.json
    # print(args)
    # if len(password)<8:
    #     return jsonify({"status":401,"error":"Password is minimun 8 character"})
    # if len(username)<3 :
    #     return jsonify({"status":401,"error":"Invalid username"})
    # if not validators.email(email):
    #     return jsonify({"status":401,"error":"Invalid email"})

    try:
        all = collection.find_one({"email":args["email"]})
        pagae = json.loads(json_util.dumps(all))
        print(pagae)
        # return "created"
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
    # username= request.json['username']
    # email=request.json['email']
    # password = request.json['password']
    args= request.json
    # print(args)
    # if len(password)<8:
    #     return jsonify({"status":401,"error":"Password is minimun 8 character"})
    # if len(username)<3 :
    #     return jsonify({"status":401,"error":"Invalid username"})
    # if not validators.email(email):
    #     return jsonify({"status":401,"error":"Invalid email"})

    try:
        all = collection.find_one({"email":args["email"],"password":args['password']})
        data = json.loads(json_util.dumps(all))
        # print(data)
        # return "created"
        if all ==None:
            return jsonify({
                "status":"400",
                "massege":"Email or Password invalid"
            }),400
       
        payload={
                'email':data['email'],
                'exp':expires
            }
        token = jwt.encode(payload, key = "secret", algorithm = "HS256")
            # print(token)
        return {
                "token":token,
                "status":200,
                "message":"Successfully login"
            },200
    except Exception as e:
        return jsonify({
            "massege":"error"+str(e)
        }),400


# @app.post('/post')
# @jwt_required
# def post():
#     args= request.json
#     # try:

#     all = collection_1.find_one({"email":args["email"]})
#     # pagae = json.loads(json_util.dumps(all))
#     # print(pagae)
#     # return "created"
#     if all == None:
#         collection_1.insert_one(args)
#     #     # var_token= headers['Authorization'] # get the token from the header
#     #     # print(var_token)
#         return "success"
#     # else:
#     #     return "already"
#     # #         token = var_token.split(" ")[1]
#     #         print(token)
#     #         if (token == None):
#     #             return("Token not found")
#             # try:
#             #     # var_decode = jwt.decode(token, key = "secret", algorithms = ['HS256'])
#             #     # print(var_decode)
#             #     collection_1.insert_one(args)
#             #     return jsonify({
#             #         "massege":"Successfully Post"}),200
#             # except jwt.ExpiredSignatureError:
#             #           return jsonify({
#             #             "massege":"Token expired"}),400

#             # except  Exception as e:
#             #    return jsonify({
#             #     "massege":"Invalid token"}),400
#     else:
#         return jsonify({
#             "massege":"email already exists"
#         }),400
#     # except Exception as e:
#     #     return jsonify({
    #         "massege":"error:"+str(e)
    #     })    


if __name__ == '__main__':
    app.run(debug=True)