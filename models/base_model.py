#!/usr/bin/python3
"""Define the BaseModel class."""
from uuid import uuid4
from datetime import datetime
import copy
from models import storage


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            self: BaseModel instance
            *args (unused): positional arguments
            **kwargs: keyword arguments
        """

        if kwargs is not None and kwargs != {}:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    self.__dict__[k] = datetime.fromisoformat(v)
                elif k != '__class__':
                    self.__dict__[k] = v
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        storage.save(self)

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = copy.deepcopy(self.__dict__)
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
