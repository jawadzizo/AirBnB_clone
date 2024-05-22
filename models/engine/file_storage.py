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

        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        try:
            f = open(FileStorage.__file_path, "r")

            objects = json.load(f)

            for k, v in objects.items():
                if v["__class__"] == "BaseModel":
                    basemodel = BaseModel(**v)
                    FileStorage.__objects[k] = basemodel
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
                    FileStorage.__objects[k] = user
                elif v["__class__"] == "State":
                    state = State()
                    if "name" in  v.keys():
                        state.name = v["name"]
                    FileStorage.__objects[k] = state
                elif v["__class__"] == "City":
                    city = City()
                    if "name" in  v.keys():
                        city.name = v["name"]
                    if "state_id" in  v.keys():
                        city.name = v["state_id"]
                    FileStorage.__objects[k] = city
                elif v["__class__"] == "Place":
                    place = Place()
                    if "name" in  v.keys():
                        place.name = v["name"]
                    if "city_id" in  v.keys():
                        place.name = v["city_id"]
                    if "user_id" in  v.keys():
                        place.name = v["user_id"]
                    if "description" in  v.keys():
                        place.name = v["description"]
                    if "number_rooms" in  v.keys():
                        place.name = int(v["number_rooms"])
                    if "number_bathrooms" in  v.keys():
                        place.name = int(v["number_bathrooms"])
                    if "max_guest" in  v.keys():
                        place.name = int(v["max_guest"])
                    if "price_by_night" in  v.keys():
                        place.name = int(v["price_by_night"])
                    if "latitude" in  v.keys():
                        place.name = float(v["latitude"])
                    if "longitude" in  v.keys():
                        place.name = float(v["longitude"])
                    if "amenity_ids" in  v.keys():
                        place.name = v["amenity_ids"]
                    FileStorage.__objects[k] = place

            f.close()

        except Exception as e:
            FileStorage.__objects = {}
