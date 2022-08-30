from wsgiref.validate import validator
from pymongo import MongoClient

client= MongoClient('mongodb://localhost:27017/')

bank = client['bank']

# def bank_employees():
schema_validators = {
   "$jsonSchema" : {
               "bsonType": "object",
               "required": ["ver","timestamp","txnid","clienttxnid","purpose","Notifier","type","id","consentId","consentHandle","Status"],
               "properties": {
                  "ver": {
                     "bsonType": "int",
                  },
                  "timestamp": {
                     "bsonType": "string",
                     "minimum": "10",
                     "maximum": "50",
                     "description": "must be a string and is required"
                  },
                  "txnid": {
                     "bsonType": "string",
                     "description": "must be a string"
                  },
                  "clienttxnid": {
                     "bsonType": "string",
                     "description": "must be a string and it is optional "
                  },
                  "purpose":{
                     "bsonType": "string",
                     "description": "must be a string",
                  },
                  "Notifier": {
                     "description": "Optional",
                  },
                  "type": {
                     "bsonType": "string",
                     "description": "must be a string and   is required",
                  },
                  "id": {
                     "bsonType": "string",
                     "description": "must be a string and   is required",
                  },
                  "consentId": {
                     "bsonType": "int",
                     "description": "must be a int and   is required",
                  },
                  "consentHandle": {
                     "bsonType": "string",
                     "description": "must be a string and   is required",
                  },
                  "Status": {
                     "bsonType": "string",
                     "description": "must be a string and   is required",
                  },
               }
               
            }
}

try:
   # db.create_collection("admin",validator=schema_validators)
   bank.create_collection("details")  # details is name of collection 
   # bank.create_collection("adimeDetails","details",validator= schema_validators_for_employees_bank)
      ##########   adimeDetails is comment , details is collection , validator = schema_validators_for employees_bank
except Exception as e:
   print(e)

# 
   # bank.command("callMod",validator=schema_validators)


# adminCol = bank["admin2"]
# # adminCol = db["employeeDetails"]
# employeeCol = bank["employeeDetails"]
# bank_employees()

# def author():
#       author_validator = {
#          "$jsonSchema":{
#             "bsonType":"object",
#             "required":["first_name","last_name","date_of_birth"],
#             "properties":{
#                "first_name":{
#                   "bsonType":"String",
#                   "description":"must be a string and is required"
#                },
#                "last_name":{
#                   "bsonType":"String",
#                   "description":"must be a string and is required"
#                },
#                "date_of_birth":{
#                   "bsonType":"date",
#                   "description":"must be a date and is required"
#                },
#             }
#          }
#       }

#       try:
#          bank.create_collection("author")

#       except Exception as e:
#          print(e)


#       # bank.command("collMod","author",validator = author_validator)

# author()

