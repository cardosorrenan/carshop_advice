import os


basedir = os.path.abspath(os.path.dirname(__file__))

user = os.environ.get('POSTGRES_USER')
password = os.environ.get('POSTGRES_PASSWORD')
host = os.environ.get('POSTGRES_HOST')
port = os.environ.get('POSTGRES_PORT')
db = os.environ.get('POSTGRES_DB')


class DatabaseConfig(object):
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False