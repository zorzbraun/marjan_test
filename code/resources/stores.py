from flask_restful import Resource, reqparse
from models.stores import StoreModel


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('store_name',type=str,required=True,help="Store_name is a required field!")
    parser.add_argument('store_country',type=str,required=True,help="Store_country is a required field!")
    parser.add_argument('store_city',type=str,required=True,help="Store_city is a required field!")
    parser.add_argument('store_address',type=str,required=True,help="Store_address is a required field!")
    parser.add_argument('store_owner',type=str,required=True,help="Store_owner is a required field!")

    def get(self, id):
        store = StoreModel.find_by_id(id)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self):
        #if StoreModel.find_by_name():
            #return {'message': f'A store with the name {store_name} already exists.'}, 400

        data = Store.parser.parse_args()
        store = StoreModel(**data)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred creating the store."}, 500

        return store.json(), 201

    def delete(self, id):
        store = StoreModel.find_by_id(id)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}

    def put(self,id):
        data = Store.parser.parse_args()
        store = StoreModel.find_by_id(id)

        if store:
            store.store_name = data['store_name']
            store.store_country = data['store_country']
            store.store_city = data['store_city']
            store.store_address = data['store_address']
            store.store_owner = data['store_owner']
        else:
            store.store_name = StoreModel(**data)
            store.store_country = StoreModel(**data)
            store.store_city = StoreModel(**data)
            store.store_address = StoreModel(**data)
            store.store_owner = StoreModel(**data)
            
        store.save_to_db()     
        return store.json()


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store  in StoreModel.query.all()]}