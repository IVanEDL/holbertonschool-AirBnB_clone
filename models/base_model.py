#!/usr/bin/python3
from uuid import uuid4
import datetime
from models import storage
class BaseModel:
    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                else:
                    try:
                        setattr(self, key, datetime.datetime.fromisoformat(value))
                    except Exception:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
    
    def save(self):
        """update"""
        storage.save()
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
