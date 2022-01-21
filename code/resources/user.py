import sqlite3
from sqlite3.dbapi2 import Cursor, connect
from flask_restful import Resource, reqparse
from models.user import UserModel

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name',type=str,required=True,help="First_name is required field.")
    parser.add_argument('last_name',type=str,required=True,help="Last_name is required field.")
    parser.add_argument('email',type=str,required=True,help="Email is required field.")
    parser.add_argument('username',type=str,required=True,help="Username is required field.")
    parser.add_argument('password',type=str,required=True,help="Password is required field.")

    def get(self,id):
        user = UserModel.find_by_id(id)
        if user:
            return user.json()
        return {'message': 'User not found.'}, 400

    def post(self): #function which creates a user within a database
        data = User.parser.parse_args()

        if UserModel.find_by_email(data['email']):
            return {'message': 'The user with this email already exists!'}, 400
        
        user = UserModel(**data)
        user.save_to_db()

        return user.json()

    def put(self, id):
        data = User.parser.parse_args()
        user = UserModel.find_by_id(id)

        if user:
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.email = data['email']
            user.username = data['username']
            user.password = data['password']
        else:
            user.first_name = UserModel(**data)
            user.last_name = UserModel(**data)
            user.email = UserModel(**data)
            user.username = UserModel(**data)
            user.password = UserModel(**data)

        user.save_to_db()     
        return user.json()

    def delete(self,id):
        user = UserModel.find_by_id(id)
        if user:
            user.delete_from_db()
            return {'message': 'User has been deleted.'}
        return {'message': 'User not found.'}, 404

class UserList(Resource):
    def get(self):
        return {'users': [user.json() for user  in UserModel.query.all()]} 