#!/usr/bin/python3
"""Class BaseModel module"""

import uuid
import datetime
from file_storage import FileStorage
storage = FileStorage()

class BaseModel:
    """"Defines BaseModel object class"""

    def __init__(self, *args, **kwargs):
        """initializes class instance"""
        if kwargs is not None and kwargs != {}:
                self.__dict__.update(kwargs)
                self.__dict__["created_at"] = datetime.datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                self.__dict__["updated__at"] = datetime.datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.my_number = None
            self.name = None
            self.updated_at = datetime.datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            storage.new(self)


    def __str__(self):
        return str("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        _dict = self.__dict__.copy()
        _dict["__class__"] = type(self).__name__
        _dict["created_at"] = _dict["created_at"].isoformat()
        _dict["updated_at"] = _dict["updated_at"].isoformat()
        return _dict
