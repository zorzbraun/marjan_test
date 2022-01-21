from flask_sqlalchemy import model
from db import db

class CarModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String(80))
    model = db.Column(db.String(80))
    manufacturing_year = db.Column(db.Integer)
    manufacturing_country = db.Column(db.String(80))
    bodystyle = db.Column(db.String(80))
    gearbox = db.Column(db.String(80))
    fuel = db.Column(db.String(80))
    color = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, manufacturer, model, manufacturing_year, manufacturing_country, bodystyle, gearbox, fuel, color, price, store_id):
        self.manufacturer = manufacturer
        self.model = model
        self.manufacturing_year = manufacturing_year
        self.manufacturing_country = manufacturing_country
        self.bodystyle = bodystyle
        self.gearbox = gearbox
        self.fuel = fuel
        self.color = color
        self.price = price
        self.store_id = store_id

    def json(self):
        return {
            'id': self.id,
            'manufacturer': self.manufacturer,
            'model': self.model,
            'manufacturing_year': self.manufacturing_year,
            'manufacturing_country': self.manufacturing_country,
            'bodystyle': self.bodystyle,
            'gearbox': self.gearbox,
            'fuel': self.fuel,
            'color': self.color,
            'price': self.price,
            'store_id': self.store_id
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first() #SELECT * FROM table_tame WHERE id=id LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()