#!/usr/bin/python3

"""This module defines tests for the User class"""


import unittest
from datetime import datetime
from models.user import User
from models import storage


class TestUserClass(unittest.TestCase):
    """Defines a Test Suite for User class"""

    def test_email_attribute(self):
        """Tests required attributes"""

        user_instance = User()

        self.assertEqual(user_instance.email, '')

    def test_first_name_attribute(self):
        """Tests required attributes"""

        user_instance = User()

        self.assertEqual(user_instance.first_name, '')

    def test_last_name_attribute(self):
        """Tests required attributes"""

        user_instance = User()

        self.assertEqual(user_instance.last_name, '')

    def test_password_attribute(self):
        """Tests required attributes"""

        user_instance = User()

        self.assertEqual(user_instance.password, '')

    def test_inherited_created_at_attribute(self):
        user_instance = User()

        self.assertIsInstance(user_instance.created_at, datetime)

    def test_inherited_updated_at_attribute(self):
        user_instance = User()

        self.assertIsInstance(user_instance.updated_at, datetime)

    def test_inherited_id_attribute(self):
        self.assertIsInstance(User().id, str)

    def test_inherited_save_method(self):
        self.assertIn('save', dir(User()))

    def test_inherited_str_method(self):
        self.assertIn("[User]", User().__str__())

    def test_inherited_str_method2(self):
        user_instance = User()

        self.assertIn(user_instance.id, user_instance.__str__())
