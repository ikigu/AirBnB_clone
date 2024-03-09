#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represent an amenity. BaseModel creates a date and time
    for when the object was instantiated and assigns an id
    to the object.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
