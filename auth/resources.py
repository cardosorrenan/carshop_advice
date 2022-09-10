
from validators import email as valid_email
from flask.json import jsonify
from flask import Blueprint, request
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

from db import db
from auth.models import User


auth = Blueprint("auth", __name__, url_prefix="/api/auth/")


@auth.post('login/')
def login():
    email = request.json.get("email", "")
    password = request.json.get("password", "")

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "Not found user."}), 400

    if not check_password_hash(user.password, password):
        return jsonify({"error": "Wrong credentials."}), 401

    refresh = create_refresh_token(identity=user.id)
    access = create_access_token(identity=user.id)

    return jsonify({"refresh": refresh,
                    "access": access,
                    "username": user.username,
                    "email": user.email
                    }), 200


@auth.post('register/')
def register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    if not valid_email(email):
        return jsonify({'error': "Email is not valid."}), 400

    pwd_hash = generate_password_hash(password)

    user = User(username=username, password=pwd_hash, email=email)
    db.session.add(user)
    db.session.commit()
    
    refresh = create_refresh_token(identity=user.id)
    access = create_access_token(identity=user.id)

    return jsonify({'refresh': refresh,
                    'access': access,
                    'username': user.username,
                    'email': user.email
                    }), 201