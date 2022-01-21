import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.user import UserList
from db import db

from security import authenticate, identity
from resources.user import User
from resources.cars import Car, CarList
from resources.stores import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'vlada'
api = Api(app)

database = db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store,'/store', '/store/<int:id>','/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Car, '/car', '/car/<int:id>')
api.add_resource(CarList, '/cars')
api.add_resource(User, '/user', '/user/<int:id>')
api.add_resource(UserList, '/users')

if __name__ == '__main__':
    app.run(debug=True ,port=5000)