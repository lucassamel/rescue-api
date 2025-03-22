from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag

from sqlalchemy.exc import IntegrityError

from model import Session, Vehicule, RescuePoint
from logger import logger
from schemas.vehicule import *
from schemas.error import ErrorSchema

info = Info(title="SOS Recue API", version="1.0.0")
app = OpenAPI(__name__, info=info)

# defining tags
home_tag = Tag(name="Documentation", description="Documentation selection screen")
vehicule_tag = Tag(name="Vehicule", description="Create, list and remove vehicules from the database")


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
        # commit the transaction
        session.commit()
        logger.debug(f"Adding a vehicule: '{vehicule.name}'")
        return get_vehicule(vehicule), 200

    except IntegrityError as e:
        # error raised from the IntegrityError
        error_msg = "Produto de mesmo nome já salvo na base :/"
        logger.warning(f"Error while adding a new vehicule: '{vehicule.name}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # other errors
        error_msg = "Error while adding a new vehicule"
        logger.warning(f"Error while adding a new vehicule: '{vehicule.name}', {e}")
        return {"message": error_msg + " " + str(e)}, 400