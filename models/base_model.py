#!/usr/bin/python3
'''
module 'base_model'
'''
import uuid
from datetime import datetime
import models
import json


class BaseModel:
    """
    BaseModel class used with all all other classes
    """

    def __init__(self, *args, **kwargs):
        '''
        class constructor for class 'BaseModel'
        '''
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key in kwargs:
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        d = datetime.strptime(kwargs[key],
                                              '%Y-%m-%dT%H:%M:%S.%f')
                        self.__dict__[key] = d
                    else:
                        self.__dict__[key] = kwargs[key]

    def __str__(self):
        '''
        string representation of BaseModel instance
        '''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        '''
        updates 'updated_at' instance with current datetime
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        dictionary representation of an instance
        '''
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
