import os

from flask.json import jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask import Flask

from db import db
from auth.routes import authorization
from config import Config
from carshop_advice.resources import ResourceOwner, ResourceCars


def create_app():
    # Setup App
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        
    # Authorization
    JWTManager(app)
    app.register_blueprint(authorization)

    # Resources
    api = Api(app)
    api.add_resource(ResourceOwner, '/api/owners/', '/api/owners/<int:id>/')
    api.add_resource(ResourceCars, '/api/cars/', '/api/cars/<int:id>/')

    # Generic Pages
    @app.errorhandler(404)
    def handle_404(e):
        return jsonify({'error': 'Not found'}), 404

    @app.errorhandler(500)
    def handle_500(e):
        return jsonify({'error': 'Something went wrong, we are working on it'}), 500

    return app


app = create_app()