#!/usr/bin/python3
"""Module containinng the class BaseModel"""
from uuid import uuid4
import datetime
import models


class BaseModel:
    """Class that defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """__init__ function doc"""
        if kwargs:
            for k, v in kwargs.items():
                if not k.startswith("_"):
                    if k in ["updated_at", "created_at"]:
                        v = datetime.datetime.fromisoformat(v)
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the object"""
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns the dictionary representation of the object"""
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = dic['created_at'].isoformat()
        dic['updated_at'] = dic['updated_at'].isoformat()
        return dic
