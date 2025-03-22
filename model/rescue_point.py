from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from  model import Base


class RescuePoint(Base):
    __tablename__ = 'rescue_point'

    id = Column("pk_rescue_point",Integer, primary_key=True)
    name = Column(String(80))
    longitude = Column(String(400))
    latitude = Column(Integer)
    inserted_date = Column(DateTime, default=datetime.now())

    # Defines a relationship between the comment and a product.
    # The column 'product' that will store the reference to the product,
    # the foreign key that relates a rescue point to vehicule.
    vehicule = Column(Integer, ForeignKey("vehicule.pk_vehicule"), nullable=True)

    def __init__(self, name:str, latitude:int = 0, longitude:int = 0, inserted_date:Union[DateTime, None] = None):
        """
        Create a recue point

        Arguments:
            name: the name of a rescue point.
            latitude: the latitude of a rescue point.
            longitude: the longitude of a rescue point.
            inserted_date: the date when the rescue point was inserted to the database.

        """
        self.name = name
        self.longitude = longitude
        self.latitude = latitude        
        if inserted_date:
            self.inseted_date = inserted_date
