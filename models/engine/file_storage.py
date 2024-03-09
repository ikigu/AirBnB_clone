#!/usr/bin/python3
"""Defines the FileStorage class for persistent object storage."""


import json
import models
import sys


class FileStorage:
    """An file storage engine for app objects.

    Class attributes:
        __file_path (str): The path to the JSON file used for storage.
        __objects (dict): Objects staging area, stores objects loaded
                          from storage and objects that need to be stored.
    """
    __file_path = "file.json"
    __objects: dict = {}

    def all(self):
        """Return class __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds an object to the staging area (__objects)"""
        object_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(object_class_name, obj.id)] = obj

    def save(self):
        """
        Serialize FileStorage.__objects to JSON
        and store the items in FileStorage.__file_path."""

        all_app_objects = FileStorage.__objects
        all_app_objects = {
            obj: all_app_objects[obj].to_dict() for obj in all_app_objects.keys()}

        with open(FileStorage.__file_path, "w") as storage_file:
            json.dump(all_app_objects, storage_file)

    def reload(self):
        """
        Deserialize app objects stored in FileStorage.__file_path,
        and load them to FileStorage.__objects
        """

        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        try:
            with open(FileStorage.__file_path) as stored_objects:
                try:
                    all_app_objects = json.load(stored_objects)
                except json.JSONDecodeError:
                    return

                for obj in all_app_objects.values():
                    obj_cls_name = obj["__class__"]
                    self.new(eval(obj_cls_name)(**obj))

        except FileNotFoundError:
            return
