#!/usr/bin/python3
"""A class FileStorage that serializes instances to a JSON file and
 deserializes JSON file to instances"""

import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Represents a class FileStorage"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary"""
        return type(self).__objects

    def new(self, obj):
        """Sets the obj in a key <obj class name>.id"""
        key = type(obj).__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in type(self).__objects.items():
            new_dict[key] = value.to_dict()
        with open(type(self).__file_path, "w") as fd:
            json.dump(new_dict, fd)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(type(self).__file_path, "r") as read_file:
                for key, value in (json.load(read_file)).items():
                    value = eval((value["__class__"]) + "(**value)")
                    type(self).__objects[key] = value
        except FileNotFoundError:
            pass
