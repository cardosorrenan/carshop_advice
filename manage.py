from flask.cli import FlaskGroup
from flask import current_app

from db import db
from carshop_advice.models import Owner, Car
from auth.models import User

from werkzeug.security import generate_password_hash


cli = FlaskGroup(current_app)

@cli.command("renew_db")
def renew_db():
    db.drop_all()
    db.create_all()
    db.session.add(User(username="usertest",
                        password=generate_password_hash("1234"),
                        email="user@test.com"))
    db.session.add(Owner(firstname="Armin",
                         lastname="Ronacher",
                         email="armin@flask.com",
                         age=33))
    db.session.add(Owner(firstname="Guido",
                         lastname="Van Rossum",
                         email="guido@python.com",
                         age=66))
    db.session.commit()
    
    db.session.add(Car(model="Hatch",
                       color="Blue",
                       available=True,
                       owner_id=1))
    db.session.add(Car(model="Convertible",
                       color="Yellow",
                       available=False,
                       owner_id=1))
    db.session.add(Car(model="Sedan",
                       color="Gray",
                       available=True,
                       owner_id=1))
    db.session.commit()


if __name__ == "__main__":
    cli()
