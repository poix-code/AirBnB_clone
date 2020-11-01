#!/usr/bin/python3
"""The base class and import modules are defined"""
import uuid
from datetime import datetime
import json


class BaseModel():
    """The instances and methods of the class are defined"""
    def __init__(self):
        """Public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Print the instances with the magic method __str__"""
        return "[{}] ({}) {}".format(BaseModel.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """Updates the public instance attribute 'updated_ at',
        with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary with the key/values of __dict__"""
        self.__dict__['__class__'] = 'BaseModel'
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__
