#!/usr/bin/python3
from uuid import uuid4
import datetime
from models import storage


class BaseModel:
    """This class is the model basis on which the web application
       will be based."""

    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                else:
                    try:
                        a = datetime.datetime.fromisoformat(value)
                        setattr(self, key, a)
                    except Exception:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def save(self):
        """update"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        r = {}
        r["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            r[key] = value
        r["created_at"] = self.created_at.isoformat()
        r["updated_at"] = self.updated_at.isoformat()
        return r

    def my_number(self, number):
        """ return a number"""
        return number

    def name(self, name):
        """ return name for the person"""
        return name
