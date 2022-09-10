import os

from flask_jwt_extended import JWTManager
from flask.json import jsonify
from flask import Flask

from db import db
from auth.resources import auth


class Config(object):
    user = os.environ.get('POSTGRES_USER')
    password = os.environ.get('POSTGRES_PASSWORD')
    host = os.environ.get('POSTGRES_HOST')
    port = os.environ.get('POSTGRES_PORT')
    db = os.environ.get('POSTGRES_DB')
    secret_key = os.environ.get('SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ALGORITHM = "HS256"
    JWT_SECRET_KEY = secret_key
    

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)
db.init_app(app)

JWTManager(app)

app.register_blueprint(auth)

@app.errorhandler(404)
def handle_404(e):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def handle_500(e):
    return jsonify({'error': 'Something went wrong, we are working on it'}), 500
