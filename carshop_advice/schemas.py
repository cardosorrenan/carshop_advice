from flask_marshmallow import Schema
from marshmallow_enum import EnumField

from carshop_advice.models import Owner, Car, CarModelChoices, CarColorChoices

class OwnerSchema(Schema):
    class Meta:
        model = Owner
        fields = ('id', 'firstname', 'lastname', 'email',
                  'age', 'created_at', 'updated_at')

owner_schema = OwnerSchema()
owners_schema = OwnerSchema(many=True)


class CarSchema(Schema):
    model = EnumField(CarModelChoices, by_value=True)
    color = EnumField(CarColorChoices, by_value=True)
    
    class Meta:
        model = Car
        fields = ('id', 'model', 'color', 'owner_id',
                  'available', 'created_at', 'updated_at')

car_schema = CarSchema()
cars_schema = CarSchema(many=True)