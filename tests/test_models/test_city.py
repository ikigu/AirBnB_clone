#!/usr/bin/python3


"""Tests the city Class"""


from datetime import datetime
from models.city import City
import unittest


class TestCityClass(unittest.TestCase):
    def test_inherited_attributes(self):
        a1 = City()

        self.assertIn('id', a1.__dict__)
        self.assertEqual('', a1.state_id)
        self.assertEqual('', a1.name)

    def test_own_attributes(self):
        a1 = City()

        self.assertIsInstance(a1.name, str)
        self.assertEqual(a1.name, '')

    def test_class_attr(self):
        self.assertIsInstance(City.name, str)

    def test_type_of_inherited_dates(self):
        self.assertIsInstance(City().created_at, datetime)
        self.assertIsInstance(City().updated_at, datetime)
        self.assertIsInstance(City().id, str)
