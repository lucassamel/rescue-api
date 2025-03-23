from pydantic import BaseModel
from model import RescuePoint
from typing import Optional, List

class RescuePointSchema(BaseModel):
    """ Defines how a new rescue point to be inserted should be represented
    """    
    name: str = "Rescue Point"
    latitude: int = 40
    longitude: int = 50  

def get_rescue_point(rescue_point: RescuePoint):
    """ Return a rescue_point object in the format of
        VechiculeSchema.
    """
    return {
        "id": rescue_point.id,
        "name": rescue_point.name,
        "latitude": rescue_point.latitude,
        "longitude": rescue_point.longitude    
    }

class RescuePointListSchema(BaseModel):
    """ Defines how a list of rescue points should be represented
    """
    produtos:List[RescuePointSchema]


def get_rescue_points(rescue_points: List[RescuePoint]):
    """ Return a list of rescue points in the format of
        RescuePointListSchema.
    """
    result = []
    for rescue_point in rescue_points:
        result.append({
            "id": rescue_point.id,	
            "name": rescue_point.name,
            "latitude": rescue_point.latitude,
            "longitude": rescue_point.longitude            
        })

    return {"rescue_points": result}

class RescuePointDeleteSchema(BaseModel):
    """ Defines how a rescue point to be deleted should be represented
    """
    id: str = "1"

class GenerateRescuePointSchema(BaseModel):
    """ Defines how a rescue point to be deleted should be represented
    """
    number: int = 50