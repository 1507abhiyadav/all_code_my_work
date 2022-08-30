# from pymongo import mongodb
from typing import Collection
import pymongo

db=pymongo.MongoClient('mongodb://localhost:27017/')
db= db['employee']  # database name
Collection = db['employee_1']