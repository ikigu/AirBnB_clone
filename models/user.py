#!/usr/bin/python3

"""Implements the User class"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    Represent a State. BaseModel creates a date and time
    for when the object was instantiated and assigns an id
    to the object.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
