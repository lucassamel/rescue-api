from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# import all models
from model.base import Base
from model.vehicule import Vehicule
from model.rescue_point import RescuePoint

db_path = "database/"
# Verify if the directory exists
if not os.path.exists(db_path):
   # create the directory if it does not exist
   os.makedirs(db_path)

# database url
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# create a configured "Engine" object
engine = create_engine(db_url, echo=False)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# cria o banco se ele não existir 
if not database_exists(engine.url):
    create_database(engine.url) 

# create all tables in the engine if they don't exist
Base.metadata.create_all(engine)
