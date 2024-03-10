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

    def test_create_class_correct_usage(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')

            object_id = f.getvalue()[:-1]
            class_name = 'User'

            stored_objects = storage.all()

            self.assertIn(f"{class_name}.{object_id}", stored_objects)

    def test_show_correct_use(self):
        object_id = ""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')

            object_id = f.getvalue()[:-1]

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show User {object_id}')

            all_objects = storage.all()

            self.assertEqual(f.getvalue()[:-1],
                             all_objects[f"User.{object_id}"].__str__())

    def test_show_no_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show')

            self.assertEqual(f.getvalue(), self.NO_CLASS_NAME)

    def test_show_class_no_exist(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show CNE')

            self.assertEqual(f.getvalue(), self.CLASS_NO_EXIST)

    def test_show_instance_no_exist(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show User BogusID')

            self.assertEqual(f.getvalue(), self.OBJ_NO_EXIST)

    def test_show_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show Amenity')

            self.assertEqual(f.getvalue(), self.ID_NOT_PASSED)

    def test_destroy_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy')

            self.assertEqual(f.getvalue(), self.NO_CLASS_NAME)

    def test_destroy_class_no_exist(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy BadClassName')

            self.assertEqual(f.getvalue(), self.CLASS_NO_EXIST)

    def test_destroy_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy Place')

            self.assertEqual(f.getvalue(), self.ID_NOT_PASSED)

    def test_show_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show Review 78d')

            self.assertEqual(f.getvalue(), self.OBJ_NO_EXIST)

    def test_destroy_correct_usage(self):
        all_objects = ""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')

            object_id = f.getvalue()[:-1]

            HBNBCommand().onecmd(f'destroy User {object_id}')

            all_objects = storage.all()

            self.assertNotIn(f"User.{object_id}", all_objects)
