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

        self.reload()
        return self.__objects

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
        from models.user import User

        try:
            f = open(self.__file_path, "r")

            objects = json.load(f)

            for k, v in objects.items():
                if v["__class__"] == "BaseModel":
                    basemodel = BaseModel(**v)
                    self.__objects[k] = basemodel
                elif v["__class__"] == "User":
                    user = User(**v)
                    if "email" in  v.keys():
                        user.email = v["email"]
                    if "password" in  v.keys():
                        user.password = v["password"]
                    if "password" in  v.keys():
                        user.first_name = v["first_name"]
                    if "last_name" in  v.keys():
                        user.last_name = v["last_name"]

                    self.__objects[k] = user

            f.close()

        except Exception as e:
            self.__objects = {}
