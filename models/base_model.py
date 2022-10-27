#!/usr/bin/python3
"""Module containinng the class BasseModel"""
from uuid import uuid4
import datetime
from models.__init__ import storage


class BaseModel:
    """Class that defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """__init__ function doc"""
        if kwargs:
            for k, v in kwargs.items():
                if not k.startswith("_"):
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the object"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary """
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = dic['created_at'].isoformat()
        dic['updated_at'] = dic['updated_at'].isoformat()
        # print("->", self.__dict__)
        return dic
