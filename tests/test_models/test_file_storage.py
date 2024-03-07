#!/usr/bin/env bash

"""Tests the storage engine"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Tests the FileStorage class"""

    # Test public instance methods
    def tests_all_method(self):
        """Tests all method"""

        base_model_instance = BaseModel()
        base_model_instance.name = "new_object"
        base_model_instance.save()
        base_model_classname = base_model_instance.to_dict()['__class__']

        all_objects = storage.all()

        self.assertEqual(
            all_objects[f"{base_model_classname}.{base_model_instance.id}"]
            .to_dict(), base_model_instance.to_dict())
