#!/usr/bin/python3
"""A class FileStorage that serializes instances to a JSON file and
 deserializes JSON file to instances"""
from models.base_model import BaseModel
import json
from datetime import datetime


class FileStorage():
    """Represents a class FileStorage"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary"""
        return self.__objects

    def new(self, obj):
        """Sets the obj in a key <obj class name>.id"""
        ob_k = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[ob_k] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as fd:
            json.dump(new_dict, fd)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding='utf-8') as read_file:
                for key, value in (json.load(read_file)).items():
                    value = eval(value["__class__"]) + "(**value)")
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
