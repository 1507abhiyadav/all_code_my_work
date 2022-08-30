# import pymongo

# client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

# mydb=client['UserDetails']

# information = mydb.Userinformation

# user_schema = {

#     'firstName': {
#         'type': 'string',
#         'minlength': 1,
#         'required': True,
#         'coerce': str.capitalize
#     },
#     'lastName': {
#         'type': 'string',
#         'minlength': 1,
#         'required': True,
#         'coerce': str.capitalize
#     },
#     'email': {
#         'type': 'string',
#         "required": False,
#         "coerce": str,
#         "nullable": True
#     },
#     'phoneNo': {
#         'type': 'integer',
#         'required': True,
#         'unique': True
#     },
#     'userId': {
#         'type': 'integer',
#         'required': True,
#         'unique': True
#     },
#     'patientId': {
#         'type': 'integer',
#         'required': True,
#         'unique': True
#     },
#     'age': {
#         'type': 'integer'
#     },
#     "userStatus": {
#         "type": "integer",
#         "nullable": True
#     }
# }

# information.insert_many(user_schema)






# from pymongo import MongoClient
# from pymongo.errors import CollectionInvalid
# from collections import OrderedDict

# db = MongoClient("mongodb://localhost:27019/")['mydatabase']

# user_schema = {
#     'firstName': {
#         'type': 'string',
#         'minlength': 1,
#         'required': True,
#     },
#     'lastName': {
#         'type': 'string',
#         'minlength': 1,
#         'required': True,
#     },
#     'email': {
#         'type': 'string',
#         "required": False,
#     },
#     'phoneNo': {
#         'type': 'int',
#         'required': True,
#     },
#     'userId': {
#         'type': 'int',
#         'required': True,
#     },
#     'patientId': {
#         'type': 'int',
#         'required': True,
#     },
#     'age': {
#         'type': 'int'
#     },
#     "userStatus": {
#         "type": "int"
#     }
# }

# collection = 'Userinformation'
# validator = {'$jsonSchema': {'bsonType': 'object', 'properties': {}}}
# required = []

# for field_key in user_schema:
#     field = user_schema[field_key]
#     properties = {'bsonType': field['type']}
#     minimum = field.get('minlength')

#     if type(minimum) == int:
#         properties['minimum'] = minimum

#     if field.get('required') is True: required.append(field_key)

#     validator['$jsonSchema']['properties'][field_key] = properties

# if len(required) > 0:
#     validator['$jsonSchema']['required'] = required

# query = [('collMod', collection),
#          ('validator', validator)]

# try:
#     db.create_collection(collection)
# except CollectionInvalid:
#     pass

# command_result = db.command(OrderedDict(query))