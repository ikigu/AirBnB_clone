#!/usr/bin/python3
"""
This module contains unit tests for the dictionary-based instantiation of BaseModel.
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelDict(unittest.TestCase):

    def test_create_from_dict(self):
        """Test creating a BaseModel instance from a dictionary."""

        original_dict = {
            "id": "12345678-90ab-cdef-1234-567890abcdef",
            "created_at": "2023-11-19T04:56:23.123456",
            "updated_at": "2023-11-20T05:07:34.456789",
            "name": "Test Name",
            "__class__": "BaseModel"  # Should be ignored during instantiation
        }

        base_model = BaseModel(**original_dict)

        # Verify attributes
        self.assertEqual(base_model.id, original_dict["id"])
        self.assertEqual(base_model.name, original_dict["name"])
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)
        self.assertEqual(base_model.created_at.isoformat(), original_dict["created_at"])
        self.assertEqual(base_model.updated_at.isoformat(), original_dict["updated_at"])

    def test_recreate_from_dict(self):
        """Test recreating a BaseModel instance from its own dictionary."""

        original_model = BaseModel()
        original_model.name = "Test Name"
        original_dict = original_model.to_dict()

        recreated_model = BaseModel(**original_dict)

        self.assertEqual(recreated_model.to_dict(), original_dict)


if __name__ == "__main__":
    unittest.main()

