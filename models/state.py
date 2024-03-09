#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represent a State. BaseModel creates a date and time
    for when the object was instantiated and assigns an id
    to the object.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
