from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Vehicule, RescuePoint
from model.rescue_point import *
from logger import logger
from schemas.vehicule import *
from schemas.rescue_point import *
from schemas.error import ErrorSchema
from flask_cors import CORS

info = Info(title="SOS Recue API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# defining tags
home_tag = Tag(name="Documentation", description="Documentation selection screen")
vehicule_tag = Tag(name="Vehicule", description="Create, list and remove vehicules from the database")
rescue_point_tag = Tag(name="Rescue Point", description="Create, list and remove rescue points from the database")

@app.get('/', tags=[home_tag])
def home():
    """Redirect to /openapi, documentation screen.
    """
    return redirect('/openapi')

@app.post('/vehicule', tags=[vehicule_tag],
          responses={"200": VehiculeSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_vehicule(form: VehiculeSchema):
    """Add a new vehicule to the database.

    Return the new vehicule added to the database.
    """
    vehicule = Vehicule(
        name=form.name,
        latitude=form.latitude,
        longitude=form.longitude)
    logger.debug(f"Creating a vehicule: '{vehicule.name}'")
    try:
        # open data base session
        session = Session()
        # adding new vehicule
        session.add(vehicule)
        # commit the changes
        session.commit()
        logger.debug(f"Adding a vehicule: '{vehicule.name}'")
        return get_vehicule(vehicule), 200

    except IntegrityError as e:
        # error raised from the IntegrityError
        error_msg = "Error while adding a new vehicule"
        logger.warning(f"Error while adding a new vehicule: '{vehicule.name}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # other errors
        error_msg = "Error while adding a new vehicule"
        logger.warning(f"Error while adding a new vehicule: '{vehicule.name}', {e}")
        return {"message": error_msg + " " + str(e)}, 400

@app.get('/vehicule', tags=[vehicule_tag],
         responses={"200": VehiculeListSchema, "404": ErrorSchema})
def get_all_vehicules():
    """Search for all vehicules in the database.

    Return a list of all vehicules.
    """
    logger.debug(f"Listing all vehicules")
    # open data base session
    session = Session()
    # get all active vehicules
    vehicules = session.query(Vehicule).filter(Vehicule.status == True).all()

    if not vehicules:
        # if there are no vehicules
        return {"vehicules": []}, 200
    else:
        logger.debug(f"%d vehicules funded" % len(vehicules))
        # return a representation of the list of vehicules
        print(vehicules)
        return get_vehicules(vehicules), 200  

@app.post('/rescue-point', tags=[rescue_point_tag],
          responses={"200": RescuePointSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_recue_point(form: RescuePointSchema):
    """Add a new rescue point to the database.

    Return the new rescue point added to the database.
    """
    rescue_point = RescuePoint(
        name=form.name,
        latitude=form.latitude,
        longitude=form.longitude)
    logger.debug(f"Creating a recue point: '{rescue_point.name}'")
    try: 
        # open data base session
        session = Session()
        # adding new rescue point
        session.add(rescue_point)
        # commit the changes
        session.commit()
        logger.debug(f"Adding a rescue point: '{rescue_point.name}'")
        return get_rescue_point(rescue_point), 200

    except IntegrityError as e:
        # error raised from the IntegrityError
        error_msg = "Error while adding a new rescue point"
        logger.warning(f"Error while adding a new rescue point: '{rescue_point.name}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # other errors
        error_msg = "Error while adding a new rescue point"
        logger.warning(f"Error while adding a new rescue point: '{rescue_point.name}', {e}")
        return {"message": error_msg + " " + str(e)}, 400

@app.post('/generate-rescue-point', tags=[rescue_point_tag],
          responses={"200": RescuePointListSchema, "409": ErrorSchema, "400": ErrorSchema})
def generate_random_rescue_points(form: GenerateRescuePointSchema):
    """Generate a several rescue points to the database.

    Return a list of new rescue points added to the database.
    """
    rescue_points = generate_rescue_points(int(form.number))
    logger.debug(f"Rescue points generated: '{rescue_points}'")
    try: 
        # open data base session
        session = Session()
        # adding new rescue point            
        session.add_all(rescue_points)
        logger.debug(f"Adding a rescue point: '{rescue_points}'")
        # commit the changes
        session.commit()        
        return get_rescue_points(rescue_points), 200

    except IntegrityError as e:
        # error raised from the IntegrityError
        error_msg = "Error while adding a new rescue point"
        logger.warning(f"Error while adding a new rescue point: '{rescue_points}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # other errors
        error_msg = "Error while adding a new rescue point"
        logger.warning(f"Error while adding a new rescue point: '{rescue_points}', {e}")
        return {"message": error_msg + " " + str(e)}, 400
    
@app.get('/rescue-point', tags=[rescue_point_tag],
         responses={"200": RescuePointListSchema, "404": ErrorSchema})
def get_all_rescue_points():
    """Search for all rescue points in the database.

    Return a list of all rescue points.
    """
    logger.debug(f"Listing all rescue points")
    # open data base session
    session = Session()
    # get all active rescue points
    rescue_points = session.query(RescuePoint).filter(RescuePoint.status == True).all()

    if not rescue_points:
        # if there are no rescue points
        return {"rescue_points": []}, 200
    else:
        logger.debug(f"%d rescue points funded" % len(rescue_points))
        # return a representation of the list of rescue points
        print(rescue_points)
        return get_rescue_points(rescue_points), 200  
    
@app.delete('/rescue-point', tags=[rescue_point_tag],
            responses={"200": RescuePointSchema, "404": ErrorSchema})
def del_rescue_point(query: RescuePointByIdSchema):
    """Delete a Rescue Point from the database based on the id

    Return the deleted rescue point.
    """
    rescue_point_id = unquote(unquote(query.id))
    print(rescue_point_id)
    logger.debug(f"Deleting the rescue point based on this id #{rescue_point_id}")
    # open data base session
    session = Session()
    # query to delete the vehicule
    rescue_point_to_update = session.query(RescuePoint).filter(RescuePoint.id == int(rescue_point_id)).first()

    if rescue_point_to_update:
        # update the object status
        rescue_point_to_update.status = False
        # commit the changes
        session.commit()
        logger.debug(f"Rescue point status updated #{rescue_point_to_update}")
        return {"message": "Rescue point deleted", "id": get_rescue_point(rescue_point_to_update)}, 200
    else:
        # if rescue point not found
        error_msg = "Rescue point not found"
        logger.warning(f"Error while delete the rescue point #{error_msg}")
        return {"message": error_msg}, 404
    
@app.get('/perform-rescue', tags=[rescue_point_tag],
            responses={"200": RescuePointSchema, "404": ErrorSchema})
def perform_recue_point(query: RescuePointByIdSchema):
    """Search for the closest rescue point to the vehicule.

    Return the closest rescue point.
    """
    vehicule_id = unquote(unquote(query.id))
    print(vehicule_id)
    logger.debug(f"Searching the closest rescue point based in the vehicule id #{vehicule_id}")
    # open data base session
    session = Session()
    # query to delete the vehicule
    vehicule = session.query(Vehicule).filter(Vehicule.id == int(vehicule_id)).first()
    rescue_points = session.query(RescuePoint).filter(RescuePoint.status == True).all()

    closest_rescue_point = closest_point(vehicule, rescue_points)

    if closest_rescue_point:
        # update the object status
        closest_rescue_point.status = False
        closest_rescue_point.vehicule = vehicule.id
        # update the vehicule with the rescue point
        vehicule.longitude = closest_rescue_point.longitude
        vehicule.latitude = closest_rescue_point.latitude
        # commit the changes
        session.commit()
        logger.debug(f"Closest rescue points #{closest_rescue_point}")
        return {"message": "Closest rescue point", "rescue_point": get_rescue_point(closest_rescue_point)}, 200
    else:
        # if rescue point not found
        error_msg = "Rescue point not found"
        logger.warning(f"Error while searching for the closest rescue point #{error_msg}")
        return {"message": error_msg}, 404
