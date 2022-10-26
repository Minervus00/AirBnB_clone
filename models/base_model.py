#!/usr/bin/python3
"""Module containinng the class BasseModel"""
from uuid import uuid4
import datetime


class BaseModel:
    """Class that defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """__init__ function doc"""
        if kwargs:
            for k, v in kwargs.items():
                if not k.startswith("_"):
                    setattr(self, k, v)
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """A string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = dic['created_at'].isoformat()
        dic['updated_at'] = dic['updated_at'].isoformat()
        # print("->", self.__dict__)
        return dic
