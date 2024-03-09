#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represent a Place. BaseModel creates a date and time
    for when the object was instantiated and assigns an id
    to the object.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids: list = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
