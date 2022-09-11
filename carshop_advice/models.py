import enum

from flask_restful import abort
from sqlalchemy.sql import func

from db import db


class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now(),
                           server_onupdate=db.func.now())


    def __repr__(self):
        return f'<Owner {self.firstname}>'
      
    
class CarModelChoices(enum.Enum):
    Hatch = "Hatch"
    Sedan = "Sedan"
    Convertible = "Convertible"


class CarColorChoices(enum.Enum):
    Blue = "Blue"
    Gray = "Gray"
    Yellow = "Yellow"


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.Enum(CarModelChoices), nullable=False)
    color = db.Column(db.Enum(CarColorChoices), nullable=False)
    available = db.Column(db.Boolean, default=False, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'),
                         nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now(),
                           server_onupdate=db.func.now())

    def check_max_cars_by_owner(self, owner_id):
        owner_cars = self.query.filter_by(owner_id=owner_id).count()
        if owner_cars >= 3:
            abort(400, message="Owner can have up to 3 cars")

    def __init__(self, **kwargs):
        owner_id = kwargs.get('owner_id')
        self.check_max_cars_by_owner(owner_id)
        super().__init__(**kwargs)
            
    def __setattr__(self, attr, value):
        if attr == 'owner_id':
            owner_id = value
            if self.owner_id != owner_id:
                self.check_max_cars_by_owner(owner_id)
        super().__setattr__(attr, value)
        

    def __repr__(self):
        return f'<Car {self.id}>'