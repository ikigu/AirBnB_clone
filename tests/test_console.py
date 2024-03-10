#!/usr/bin/python3


"""Tests the console module"""


import unittest
import sys
import os
from unittest.mock import patch
from models import storage
from io import StringIO
HBNBCommand = __import__('console').HBNBCommand


class TestConsole(unittest.TestCase):
    """Tests"""

    @classmethod
    def setUp(cls):
        cls.NO_CLASS_NAME = "** class name missing **\n"
        cls.CLASS_NO_EXIST = "** class doesn't exist **\n"
        cls.ID_NOT_PASSED = "** instance id missing **\n"
        cls.OBJ_NO_EXIST = "** no instance found **\n"
        cls.NO_ATTR_KEY = "** attribute name missing **\n"
        cls.NO_ATTR_VALUE = "** value missing **\n"

    def tearDown(self):
        if os.path.isfile('file.json'):
            os.remove('file.json')

    def test_create_no_arguments(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create')

            self.assertEqual(f.getvalue(), self.NO_CLASS_NAME)

    def test_create_class_name_no_exist(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create NonExistentClass')

            self.assertEqual(f.getvalue(), self.CLASS_NO_EXIST)

    def test_create_class_User(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')

            object_id = f.getvalue()[:-1]
            class_name = 'User'

            stored_objects = storage.all()

            self.assertIn(f"{class_name}.{object_id}", stored_objects)

    def test_create_class_Amenity(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Amenity')

            object_id = f.getvalue()[:-1]
            class_name = 'Amenity'

            stored_objects = storage.all()

            self.assertIn(f"{class_name}.{object_id}", stored_objects)
