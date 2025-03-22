from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """ Defines the error message to be returned
    """
    mesage: str
