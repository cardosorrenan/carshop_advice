from flask_restful import Resource, request
from flask_jwt_extended import jwt_required
from flasgger import swag_from

from carshop_advice.models import Owner, Car
from carshop_advice.schemas import owner_schema, owners_schema, \
                                   car_schema, cars_schema

from db import db

    
class ResourceOwners(Resource):
    
    @jwt_required()
    @swag_from('docs/owners/list.yml')
    def get(self):
        owners = Owner.query.all()
        return owners_schema.dump(owners)
    
    @jwt_required()
    @swag_from('docs/owners/create.yml')
    def post(self):
        payload = request.json
        new_owner = Owner(
            firstname=payload['firstname'],
            lastname=payload['lastname'],
            email=payload['email'],
            age=payload['age'],
        )
        db.session.add(new_owner)
        db.session.commit()
        return owner_schema.dump(new_owner), 201   

class ResourceOwner(Resource):
    
    @jwt_required()
    @swag_from('docs/owners/get_one.yml')
    def get(self, id):
        owner = Owner.query.get_or_404(id)
        return owner_schema.dump(owner), 200
    
    @jwt_required()
    @swag_from('docs/owners/update.yml')
    def patch(self, id):
        owner = Owner.query.get_or_404(id)
        payload = request.json
        if 'firstname' in payload:
            owner.firstname = payload['firstname']
        if 'lastname' in payload:
            owner.lastname = payload['lastname']
        if 'email' in payload:
            owner.email = payload['email']
        if 'age' in payload:
            owner.age = payload['age']

        db.session.commit()
        return owner_schema.dump(owner), 200
    
    @jwt_required()
    @swag_from('docs/owners/delete.yml')
    def delete(self, id):
        owner = Owner.query.get_or_404(id)
        db.session.delete(owner)
        db.session.commit()
        return '', 204

    
class ResourceCars(Resource):
    
    @jwt_required()
    @swag_from('docs/cars/list.yml')
    def get(self):
        availables = request.args.get('availables', 0)
        if availables:
            cars = Car.query.filter_by(available=availables)
            return cars_schema.dump(cars)
        else:
            cars = Car.query.all()
            return cars_schema.dump(cars)
    

    @jwt_required()
    @swag_from('docs/cars/create.yml')
    def post(self):
        payload = request.json
        new_car = Car(
            model=payload['model'],
            color=payload['color'],
            available=payload['available'],
            owner_id=payload['owner_id'],
        )
        db.session.add(new_car)
        db.session.commit()
        return car_schema.dump(new_car), 201
    

class ResourceCar(Resource):
    
    @jwt_required()
    @swag_from('docs/cars/get_one.yml')
    def get(self, id):
        car = Car.query.get_or_404(id)
        return car_schema.dump(car), 200
    
    @jwt_required()
    @swag_from('docs/cars/update.yml')
    def patch(self, id):
        car = Car.query.get_or_404(id)
        payload = request.json
        
        if 'model' in payload:
            car.model = payload['model']
        if 'color' in payload:
            car.color = payload['color']
        if 'available' in payload:
            car.available = payload['available']
        if 'owner_id' in payload:
            car.owner_id = payload['owner_id']

        db.session.commit()
        return car_schema.dump(car), 200
    
    @jwt_required()
    @swag_from('docs/cars/delete.yml')
    def delete(self, id):
        car = Car.query.get_or_404(id)
        db.session.delete(car)
        db.session.commit()
        return '', 204