from flask import Flask
from db import DatabaseConfig
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(DatabaseConfig)
db = SQLAlchemy(app)