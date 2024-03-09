#!/usr/bin/python3


"""Tests the state Class"""


from datetime import datetime
from models.state import State
import unittest


class TestStateClass(unittest.TestCase):
    def test_inherited_attributes(self):
        a1 = State()

        self.assertIn('id', a1.__dict__)
        self.assertEqual('', a1.name)

    def test_own_attributes(self):
        a1 = State()

        self.assertIsInstance(a1.name, str)
        self.assertEqual(a1.name, '')

    def test_class_attr(self):
        self.assertIsInstance(State.name, str)

    def test_type_of_inherited_dates(self):
        self.assertIsInstance(State().created_at, datetime)
        self.assertIsInstance(State().updated_at, datetime)
        self.assertIsInstance(State().id, str)
