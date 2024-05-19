#!/usr/bin/python3
"""
serializes instances to a JSON file and deserializes JSON file to instances
"""

import json


class FileStorage:
    """a class for the storage mechanism"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """

        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """

        objects = {}

        for k, v in FileStorage.__objects.items():
            objects[k] = v.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(objects, f, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """

        from models.base_model import BaseModel

        try:
            f = open(FileStorage.__file_path, "r")

            objects = json.load(f)

            for k, v in objects.items():
                FileStorage.__objects[k] = BaseModel(**v)

            f.close()

        except Exception:
            pass
