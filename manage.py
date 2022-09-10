from flask.cli import FlaskGroup
from flask import current_app

from db import db
from carshop_advice.models import Owner, Car


cli = FlaskGroup(current_app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

        
@cli.command("seed_db")
def seed_db():
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
