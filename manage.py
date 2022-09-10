from flask.cli import FlaskGroup

from app import app, db
from carshop_advice.models import Owner, Car


cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

        
@cli.command("seed_db")
def seed_db():
    db.session.add(Owner(firstname="Armin",
                         lastname="Ronacher",
                         email="armin_ronacher@flask.com",
                         age=33))
    db.session.commit()
    
    db.session.add(Car(model="HATCH",
                       color="BLUE",
                       available=True,
                       owner_id=1))
    db.session.add(Car(model="CONVERTIBLE",
                       color="YELLOW",
                       available=False,
                       owner_id=1))
    db.session.add(Car(model="SEDAN",
                       color="GRAY",
                       available=True,
                       owner_id=1))
    db.session.commit()


if __name__ == "__main__":
    cli()
