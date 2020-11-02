#!/usr/bin/python3
"""The base class and import modules are defined"""
import uuid
from datetime import datetime
import json
import models


class BaseModel():
    """The instances and methods of the class are defined"""
    def __init__(self, *args, **kwargs):
        """Public instance attributes"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
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
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary with the key/values of __dict__"""
        cpy = self.__dict__.copy()
        cpy['__class__'] = 'BaseModel'
        cpy['created_at'] = self.created_at.isoformat()
        cpy['updated_at'] = self.updated_at.isoformat()
        return cpy
