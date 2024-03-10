#!/usr/bin/python3
"""Define the BaseModel class."""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel. When kwargs are not passed,
        a new object is created. Kwargs is passed when the
        object is getting recreated from file storage.

        Args:
            self: BaseModel instance
            *args: unused positional arguments
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
            self.updated_at = self.created_at
            storage.new(self)

    def save(self):
        """
        Updates updated_at attribute with the current
        datetime and writes the instance to file.
        """
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """
        Creates an extended dict representation of a BaseModel instance
        by adding a key/value pair -> __class__: <class_name>

        Args:
            self: represents the object instance
        """
        extended_dict = self.__dict__.copy()
        extended_dict["created_at"] = self.created_at.isoformat()
        extended_dict["updated_at"] = self.updated_at.isoformat()
        extended_dict["__class__"] = self.__class__.__name__

        return extended_dict

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        clname = self.__class__.__name__

    @classmethod
    def count(cls):
        """
        Prints a count of objects in storage that are of this class.
        """

        all_objs = storage.all()
        count = 0

        for k, v in all_objs.items():

            if all_objs[k].to_dict()['__class__'] == cls.__name__:
                count += 1

        print(count)

    @classmethod
    def all(cls):
        """
        Fetches all instances of subclasses
        of this class from storage and prints them.
        """

        all_objs = storage.all()
        all_objs_of_class = []

        for k, v in all_objs.items():

            if all_objs[k].to_dict()['__class__'] == cls.__name__:
                all_objs_of_class.append(all_objs[k])

        print('[', end="")

        for i in range(0, len(all_objs_of_class)):
            print(all_objs_of_class[i], end="")

            if i != len(all_objs_of_class) - 1:
                print(", ", end="")

        print(']')
