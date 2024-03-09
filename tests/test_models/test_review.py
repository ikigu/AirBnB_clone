#!/usr/bin/python3

"""Tests the review Class"""


from datetime import datetime
from models.review import Review
import unittest


class TestReviewClass(unittest.TestCase):
    def test_inherited_attributes(self):
        a1 = Review()

        self.assertIn('id', a1.__dict__)
        self.assertEqual('', a1.place_id)
        self.assertEqual('', a1.user_id)

    def test_place_id_attr(self):
        self.assertIsInstance(Review.place_id, str)

    def test_user_id_attr(self):
        self.assertIsInstance(Review.user_id, str)

    def test_text_attr(self):
        self.assertIsInstance(Review.text, str)

    def test_type_of_inherited_dates(self):
        self.assertIsInstance(Review().created_at, datetime)
        self.assertIsInstance(Review().updated_at, datetime)
        self.assertIsInstance(Review().id, str)
