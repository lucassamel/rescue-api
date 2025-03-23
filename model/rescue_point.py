from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from datetime import datetime
from typing import Union
import random

from  model import Base


class RescuePoint(Base):
    __tablename__ = 'rescue_point'

    id = Column("pk_rescue_point",Integer, primary_key=True)
    name = Column(String(80))
    longitude = Column(String(400))
    latitude = Column(Integer)
    inserted_date = Column(DateTime, default=datetime.now())
    status =Column(Boolean, default=True)

    # Defines a relationship between the comment and a product.
    # The column 'product' that will store the reference to the product,
    # the foreign key that relates a rescue point to vehicule.
    vehicule = Column(Integer, ForeignKey("vehicule.pk_vehicule"), nullable=True)

    def __init__(self, name:str, latitude:int = 0, longitude:int = 0, status:bool = True, inserted_date:Union[DateTime, None] = None):
        """
        Create a recue point

        Arguments:
            name: the name of a rescue point.
            latitude: the latitude of a rescue point.
            longitude: the longitude of a rescue point.
            inserted_date: the date when the rescue point was inserted to the database.
            status: the status of the rescue point.
        """
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
        self.status = status        
        if inserted_date:
            self.inseted_date = inserted_date

def generate_rescue_points(quantity:int, min_val:int=-100, max_val:int=100):
    """
        Generate a several rescue points.

        Arguments:
            quantity: the quantity of rescue points that will be generated.                       
        """
    rescue_points = [(random.randint(min_val, max_val), random.randint(min_val, max_val)) for _ in range(quantity)]

    result = []
    for index, rescue_point in enumerate(rescue_points):                   
        result.append(RescuePoint(           	
            name= f"Rescue Point {index + 1}",
            latitude= rescue_point[0],
            longitude= rescue_point[1]            
        ))

    return result