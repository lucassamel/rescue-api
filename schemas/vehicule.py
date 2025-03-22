from pydantic import BaseModel

from model import Vehicule


class VehiculeSchema(BaseModel):
    """ Defines how a new vehicule to be inserted should be represented
    """    
    name: str = "Car XPTO"
    latitude: int = 40
    longitude: int = 50

def get_vehicule(vehicule: Vehicule):
    """ Return a vehicule object in the format of
        VechiculeSchema.
    """
    return {
        "id": vehicule.id,
        "name": vehicule.name,
        "latitude": vehicule.latitude,
        "longitude": vehicule.longitude    
    }