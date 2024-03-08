#!/usr/bin/python3

"""Implements the User class"""


from models.base_model import BaseModel


class User(BaseModel):
    """The user class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
