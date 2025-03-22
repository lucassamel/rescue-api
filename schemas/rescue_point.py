from pydantic import BaseModel


class RescuePoint(BaseModel):
    """ Defines how a new rescue point to be inserted should be represented
    """
    rescue_point_id: int = 1
    name: str = "Rescue Point"
    latitude: int = 40
    longitude: int = 50
