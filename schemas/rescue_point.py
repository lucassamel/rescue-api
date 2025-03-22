from pydantic import BaseModel
from model import RescuePoint

class RescuePointSchema(BaseModel):
    """ Defines how a new rescue point to be inserted should be represented
    """
    rescue_point_id: int = 1
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