#!/usr/bin/python3


"""Tests the place Class"""


from datetime import datetime
from models import storage
from models.place import Place
import unittest


class TestPlaceClass(unittest.TestCase):
    def test_inherited_attributes(self):
        a1 = Place()

        self.assertIn('id', a1.__dict__)
        self.assertIn('created_at', a1.__dict__)
        self.assertIn('updated_at', a1.__dict__)

    def test_city_id_attributes(self):
        self.assertIsInstance(Place.city_id, str)

    def test_user_id_attribute(self):
        self.assertIsInstance(Place.user_id, str)

    def test_name_attribute(self):
        self.assertIsInstance(Place.name, str)

    def test_description_attribute(self):
        self.assertIsInstance(Place.description, str)

    def test_number_rooms_attribute(self):
        self.assertIsInstance(Place.number_rooms, int)

    def test_number_bathrooms_attribute(self):
        self.assertIsInstance(Place.number_bathrooms, int)

    def test_max_guest_attribute(self):
        self.assertIsInstance(Place.max_guest, int)

    def test_price_by_night_attribute(self):
        self.assertIsInstance(Place.price_by_night, int)

    def test_latitude_attribute(self):
        self.assertIsInstance(Place.latitude, float)

    def test_longitude_attribute(self):
        self.assertIsInstance(Place.longitude, float)

    def test_amenity_ids_attribute(self):
        self.assertIsInstance(Place.amenity_ids, list)

    def test_class_attr(self):
        self.assertIsInstance(Place.name, str)

    def test_type_of_inherited_dates(self):
        self.assertIsInstance(Place().created_at, datetime)
        self.assertIsInstance(Place().updated_at, datetime)
        self.assertIsInstance(Place().id, str)

    def test_save_method(self):
        p1 = Place()

        p1.save()
        all_objects = storage.all()

        self.assertIn(f"Place.{p1.id}", all_objects)
