from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(80))
    store_country = db.Column(db.String(80))
    store_city = db.Column(db.String(80))
    store_address = db.Column(db.String(200))
    store_owner = db.Column(db.String(80))
    cars = db.relationship('CarModel', lazy='dynamic')

    def __init__(self, store_name, store_country, store_city, store_address, store_owner):
        self.store_name = store_name
        self.store_country = store_country
        self.store_city = store_city
        self.store_address = store_address
        self.store_owner = store_owner

    def json(self):
        return {
            'id': self.id,
            'store_name': self.store_name,
            'store_country': self.store_country,
            'store_city': self.store_city,
            'store_address': self.store_address,
            'store_owner': self.store_owner
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_name(cls,store_name):
        return cls.query.filter_by(store_name=store_name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()