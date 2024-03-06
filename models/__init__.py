#!/usr/bin/python3
"""__init__ method for models directory"""

from models.engine.file_storage import FileStorage

"""Create a single instance of the FileStorage class for the entire application"""
storage = FileStorage()

"""Load previously saved objects from the storage file (if it exists)"""
storage.reload()

