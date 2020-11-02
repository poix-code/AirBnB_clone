#!/usr/bin/python3
"""The base class and import modules are defined"""
import uuid
from datetime import datetime
import json


class BaseModel():
    """The instances and methods of the class are defined"""
    def __init__(self, name=None, my_number=None, *args, **kwargs):
        """Public instance attributes"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for i in kwargs:
                if i == '__class__':
                    continue
                if i in ('updated_at', 'created_at'):
                    dt = datetime.strptime(kwargs[i], '%Y-%m-%dT%H:%M:%S.%f')
                    self.__dict__[i] = dt
                else:
                    self.__dict__[i] = kwargs[i]

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
