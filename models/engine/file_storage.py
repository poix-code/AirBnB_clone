#!/usr/bin/python3
"""The base class and import modules are defined"""
import json
from models.base_model import BaseModel


class FileStorage():
    """The instances and methods of the class are defined"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """Sets the obj in a key <obj class name>.id"""
        ob_k = obj.__class__.__name__ + '.' + obj.id
        self.__objects[ob_k] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        objs = {}
        for key, value in self.__objects.items():
            objs[key] = value.to_dict()
            with open(self.__file_path, 'w', encoding='utf-8') as fd:
                json.dump(objs, fd)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as fd:
                for key, value in (json.load(fd)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
