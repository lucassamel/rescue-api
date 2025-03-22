from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from  model import Base


class Vehicule(Base):
    __tablename__ = 'vehicule'

    id = Column("pk_vehicule",Integer, primary_key=True)
    name = Column(String(80))
    longitude = Column(Integer)
    latitude = Column(Integer)
    inseted_date = Column(DateTime, default=datetime.now())    

    def __init__(self, name:str, latitude:int = 0, longitude:int = 0, inserted_date:Union[DateTime, None] = None):
        """
        Create a vehicule

        Arguments:
            name: the name of a vehicule.
            latitude: the latitude of a rescue point.
            longitude: the longitude of a rescue point.
            inserted_date: the date when the vehicule was inserted to the database.

        """
        self.name = name
        self.longitude = longitude
        self.latitude = latitude        
        if inserted_date:
            self.inseted_date = inserted_date
