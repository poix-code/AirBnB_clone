#!/usr/bin/python3
"""A class FileStorage that serializes instances to a JSON file and
 deserializes JSON file to instances"""

import json
import os

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
        key = "{}.{}".format(obj.__class__.__name__+'.'+obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as write_file:
            write_file.write(json.dump(new_dict))

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as read_file:
                for key, value in temp.items():
                    temp_value = models.clases[value["__class__"]](**value)
                    self.__objects[key] = temp_value
        except FileNotFoundError:
            pass
