#!/usr/bin/python3
"""A class FileStorage that serializes instances to a JSON file and
 deserializes JSON file to instances"""

from models.base_model import BaseModel
from models.user import User
import json
from datetime import datetime
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """Represents a class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary"""
        return type(self).__objects

    def new(self, obj):
<<<<<<< HEAD
        """Sets the obj in a key <obj class name>.id"""
        ob_k = obj.__class__.__name__ + '.' + str(obj.id)
        self.__objects[ob_k] = obj
=======
        """sets in objects"""
        key = type(obj).__name__ + '.' + obj.id
        type(self).__objects[key] = obj
>>>>>>> 509c4826929b96f1b58fb5e263a3ac96872cb248

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w",
                  encoding='utf-8') as write_file:
            json.dump(new_dict, write_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r",
                      encoding='utf-8') as read_file:
                type(self).__objects = json.load(read_file)
            for key, value in type(self).__objects.items():
                obj = eval(type(self).__objects[key]['__class__'])(**value)
                type(self).__objects[key] = obj

        except FileNotFoundError:
            pass
