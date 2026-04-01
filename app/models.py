from . import db

class Properties(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(700))
    bedrooms = db.Column(db.Integer())
    bathrooms = db.Column(db.Integer())
    location = db.Column(db.String(120))
    price = db.Column(db.Integer())
    type = db.Column(db.String(10))
    photo = db.Column(db.String(200))

    def __init__(self, id, title, description, bedrooms, bathrooms, location, price, type, photo):
        self.id = id
        self.title = title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.type = type
        self.photo = photo
