#!/usr/bin/python3
"""Models package initialization"""

from models.engine.file_storage import FileStorage

"""Create a single instance of FileStorage object"""
storage = FileStorage()

"""Load previously saved objects from the storage file,
file.json, if it exists
"""
storage.reload()
