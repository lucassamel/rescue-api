from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
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
    status = Column(Boolean, default=True) 

    def __init__(self, name:str, latitude:int = 0, longitude:int = 0, status: bool = True, inserted_date:Union[DateTime, None] = None):
        """
        Create a vehicule

        Arguments:
            name: the name of a vehicule.
            latitude: the latitude of a rescue point.
            longitude: the longitude of a rescue point.
            inserted_date: the date when the vehicule was inserted to the database.
            status: the status of the vehicule.

        """
        self.name = name
        self.longitude = longitude
        self.latitude = latitude        
        self.status = status
        if inserted_date:
            self.inseted_date = inserted_date
