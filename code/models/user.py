from enum import unique
import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80),)
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password

    def json(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.last_name,
            'username': self.username,
            'password': self.password
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
 
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()