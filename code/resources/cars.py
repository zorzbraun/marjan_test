from os import name
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.cars import CarModel


class Car(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('manufacturer',type=str,required=True,help="Manufacturer is required field!")
    parser.add_argument('model',type=str,required=True,help="Model is required field!")
    parser.add_argument('manufacturing_year',type=int,required=True,help="Every car has a manufacturing_year.")
    parser.add_argument('manufacturing_country',type=str,required=True,help="We have to know where this car is made.")
    parser.add_argument('bodystyle',type=str,required=True,help="Please tell us what is the bodystyle of the car.")
    parser.add_argument('gearbox',type=str,required=True,help="You have to specify the gearbox type of the car.")                   
    parser.add_argument('fuel',type=str,required=True,help="Fuel is important field. Tell us what your car burns.")
    parser.add_argument('color',type=str,required=True,help="Please enter the color of the car.")
    parser.add_argument('price',type=float,required=True,help="Should you wisht to sell the car, we have to know the price.")
    parser.add_argument('store_id',type=int,required=True,help="Every car is stored somewhere. Please share which store is it.")                   

    def get(self, id):
        car = CarModel.find_by_id(id)
        if car:
            return car.json()
        return {'message': 'Car not found'}, 404

    def post(self):
        data = Car.parser.parse_args()
        car = CarModel(**data)
        try:
            car.save_to_db()
        except:
            return{'message': 'An error occured inserting the item'}, 500 #internal server error
        return car.json(), 201
 
    def delete(self,id):
        car = CarModel.find_by_id(id)
        if car:
            car.delete_from_db()
            return {'message': 'Car has been deleted'}
        return {'message': 'Car not found'}, 404

    def put(self, id):
        data = Car.parser.parse_args()
        car = CarModel.find_by_id(id)

        if car:
            car.manufacturer = data['manufacturer']
            car.model = data['model']
            car.manufacturing_year = data['manufacturing_year']
            car.manufacturing_country = data['manufacturing_country']
            car.bodystyle = data['bodystyle']
            car.gearbox = data['gearbox']
            car.fuel = data['fuel']
            car.color = data['color']
            car.price = data['price']
        else:
            car.manufacturer = CarModel(**data)
            car.model = CarModel(**data)
            car.manufacturing_year = CarModel(**data)
            car.manufacturing_country = CarModel(**data)
            car.bodystyle = CarModel(**data)
            car.gearbox = CarModel(**data)
            car.fuel = CarModel(**data)
            car.color = CarModel(**data)
            car.price = CarModel(**data)

        car.save_to_db()     
        return car.json()


class CarList(Resource):
    def get(self):
        return {'cars': [car.json() for car  in CarModel.query.all()]}