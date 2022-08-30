from db import db

class User(db.Model):
    id = db.collection(db.Integer, primary_key=True)
    email = db.collection(db.Text, unique=True, nullable=False)
    hash = db.collection(db.Text, nullable=False)