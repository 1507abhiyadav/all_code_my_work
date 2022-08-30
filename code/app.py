from gc import collect
from http import client
import pymongo
try:
	client=pymongo.MongoClient('mongodb://localhost:27017/')
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")


mydb = client['employee']  # database name
collection = mydb['employee']  # collection name
information = mydb.employeeinformation
record =({
    "name":"abc",
    "age":23,
    "phone":"7777"
},
{
    "name":"sdfghj",
    "age":233,
    "phone":"8888"
})

### insert data in database --->
# information.insert_one(record)
# print(information)
# information.insert_many(record)
# print(information)



## find all data in database--->
# all = information.find()
# for record in all:
#     print(record)


### update data in database ---->
# information.update_one({"name":"abc"},{"$set":{"name":"abhishek"}})
# information.update_many()


### delete data from database--->
# information.delete_one({"phone":"xuyy7xxx"}) #
information.delete_many({}) ## delete all data from database
