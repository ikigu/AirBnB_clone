#!/usr/bin/python3


"""Tests the amenity Class"""


from datetime import datetime
from models.amenity import Amenity
import unittest


class TestAmenityClass(unittest.TestCase):
    def test_inherited_attributes(self):
        a1 = Amenity()

        self.assertIn('id', a1.__dict__)
        self.assertIn('created_at', a1.__dict__)
        self.assertIn('updated_at', a1.__dict__)

    def test_own_attributes(self):
        a1 = Amenity()

        self.assertIsInstance(a1.name, str)
        self.assertEqual(a1.name, '')

    def test_class_attr(self):
        self.assertIsInstance(Amenity.name, str)

    def test_type_of_inherited_dates(self):
        self.assertIsInstance(Amenity().created_at, datetime)
        self.assertIsInstance(Amenity().updated_at, datetime)
        self.assertIsInstance(Amenity().id, str)
