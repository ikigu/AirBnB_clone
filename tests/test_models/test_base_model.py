#!/usr/bin/python3

"""
This module contains unit tests for the Base class of our models.
"""

from models.base_model import BaseModel
from datetime import datetime
import models
import unittest


class TestBaseClass(unittest.TestCase):
    """Tests Base class"""

    # Test documentation
    def test_module_documentation(self):
        """Test documentation exists for base_model module"""
        self.assertTrue(len(models.base_model.__doc__) > 1)

    def test_base_class_documentation(self):
        """Test documentation exists for BaseModel class"""
        self.assertTrue(len(BaseModel.__doc__) > 1)

    def test_init_method_documentation(self):
        """Test that BaseModel's init method is documented"""
        self.assertTrue(len(BaseModel.__init__.__doc__) > 1)

    def test_str_documentation(self):
        """Test that BaseModel's __str__ method is documented"""
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)

    # Test that attributes exist
    def test_has_id(self):
        """Test that BaseModel instance has id attribute"""

        b1 = BaseModel()

        self.assertTrue('id' in b1.__dict__)

    def test_has_created_at(self):
        """Test that BaseModel instance has created_at attribute"""

        b1 = BaseModel()
        self.assertTrue('created_at' in b1.__dict__)

    def test_has_updated_at(self):
        """Test that BaseModel instance has updated_at attribute"""

        b1 = BaseModel()
        self.assertTrue('updated_at' in b1.__dict__)

    # Test required attribute types
    def test_id_type(self):
        """Test that BaseModels instance attribute id is string"""

        b1 = BaseModel()

        self.assertIsInstance(b1.id, str)

    def test_created_at_type(self):
        """Test that created_at is datetime"""

        b1 = BaseModel()

        self.assertIsInstance(b1.created_at, datetime)

    def test_updated_at_type(self):
        """Test that updated_at is datetime"""

        b1 = BaseModel()

        self.assertIsInstance(b1.updated_at, datetime)

    # Test that ids are unique
    def test_ids_are_unique(self):
        """Tests that ids are unique for each BaseModel"""

        b1 = BaseModel()
        b2 = BaseModel()

        self.assertNotEqual(b1.id, b2.id)

    # Test other methods
    # def test_str_method(self):
    #     """Test __str__ method output"""

    #     b1 = BaseModel()

    #     search_string = "\A\[\w+\] \((\w+-){4}\w+\) \{.+}"
    #     match_object = re.search(search_string, b1.__str__())

    #     self.assertTrue(match_object is not None)

    def test_save_method(self):
        """Test that save method changes the updated_at attribute"""

        b1 = BaseModel()
        old_date = b1.updated_at
        b1.save()
        new_date = b1.updated_at

        delta = new_date - old_date

        self.assertTrue(delta.microseconds > 0)

    def test_todict_method(self):
        """Test that todict returns dictionary representation of instance"""

        b1 = BaseModel()
        extended_dict = b1.__dict__.copy()
        extended_dict['__class__'] = BaseModel.__name__
        extended_dict['created_at'] = extended_dict['created_at'].isoformat()
        extended_dict['updated_at'] = extended_dict['updated_at'].isoformat()

        self.assertEqual(b1.to_dict(), extended_dict)


class TestBaseModelDict(unittest.TestCase):

    def test_create_from_dict(self):
        """Test creating a BaseModel instance from a dictionary."""

        original_dict = {
            "id": "12345678-90ab-cdef-1234-567890abcdef",
            "created_at": "2023-11-19T04:56:23.123456",
            "updated_at": "2023-11-20T05:07:34.456789",
            "name": "Test Name",
            "__class__": "BaseModel"
        }

        base_model = BaseModel(**original_dict)

        self.assertEqual(base_model.id, original_dict["id"])
        self.assertEqual(base_model.name, original_dict["name"])
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)
        self.assertEqual(base_model.created_at.isoformat(),
                         original_dict["created_at"])
        self.assertEqual(base_model.updated_at.isoformat(),
                         original_dict["updated_at"])

    def test_recreate_from_dict(self):
        """Test recreating a BaseModel instance from its own dictionary."""

        original_model = BaseModel()
        original_model.name = "Test Name"
        original_dict = original_model.to_dict()

        recreated_model = BaseModel(**original_dict)

        self.assertEqual(recreated_model.to_dict(), original_dict)


if __name__ == "__main__":
    unittest.main()
