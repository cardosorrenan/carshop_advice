import enum

from db import db

from sqlalchemy.sql import func


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
    HATCH = "Hatch"
    SEDAN = "Sedan"
    CONVERTIBLE = "Convertible"


class CarColorChoices(enum.Enum):
    BLUE = "Blue"
    GRAY = "Gray"
    YELLOW = "Yellow"


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.Enum(CarModelChoices))
    color = db.Column(db.Enum(CarColorChoices))
    available = db.Column(db.Boolean, default=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'),
                         nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now(),
                           server_onupdate=db.func.now())


    def __repr__(self):
        return f'<Car {self.model}({self.color})>'