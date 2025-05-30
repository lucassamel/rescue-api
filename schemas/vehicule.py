from pydantic import BaseModel, ConfigDict
from typing import Optional, List

from model import Vehicule

class VehiculeSchema(BaseModel):
    
    # model_config = ConfigDict(coerce_numbers_to_str=True)

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

class VehiculeListSchema(BaseModel):
    """ Defines how a list of vehicules should be represented
    """
    vehicules:List[VehiculeSchema]


def get_vehicules(vehicules: List[Vehicule]):
    """ Return a list of vehicules in the format of
        VehiculeListSchema.
    """
    result = []
    for vehicule in vehicules:
        result.append({
            "id": vehicule.id,	
            "name": vehicule.name,
            "latitude": vehicule.latitude,
            "longitude": vehicule.longitude            
        })

    return {"vehicules": result}

class VehiculeDeleteSchema(BaseModel):
    """ Defines how a vehicule to be deleted should be represented
    """
    id: str = "1"