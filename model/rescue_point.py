from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from datetime import datetime
from typing import Union, List
from model import Vehicule

import random

from  model import Base


class RescuePoint(Base):
    __tablename__ = 'rescue_point'

    id = Column("pk_rescue_point",Integer, primary_key=True)
    name = Column(String(80))
    longitude = Column(Integer)
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

# This function is used to calculate the distance between two points.
# It uses the Euclidean distance formula.
def calculate_distance(point1: Vehicule, point2: RescuePoint):
    return ((point1.latitude - point2.latitude)**2 + (point1.longitude - point2.longitude)**2)**0.5

@staticmethod
def closest_point(reference_point: Vehicule, points: List[RescuePoint]):
    next_point = points[0]
    shortest_distance = calculate_distance(reference_point, next_point)

    for point in points[1:]:
        distance = calculate_distance(reference_point, point)
        if distance < shortest_distance:
            shortest_distance = distance
            next_point = point

    return next_point