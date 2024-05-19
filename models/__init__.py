#!/usr/bin/python3
""" Module to make this directory as a package
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
