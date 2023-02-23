#!/usr/bin/python3
from uuid import uuid4
import datetime
class BaseModel:
    def __init__(self, id=None):
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def save(self):
        """update"""
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) ({self.__dict__})"
    
    def to_dict(self):
        r = {}
        r ["__class__"] = __class__.__name__
        for key, value in self.__dict__.items():
            if type(value) is not int:
                r[key] = str(value)
            else:
                r[key] = value
        return r
   
   
    def my_number(self, number):
        return number
   
    def name(self,name):
        return name
