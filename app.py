from flask import Flask
from db import DatabaseConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(DatabaseConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)