#!/usr/bin/python3
"""
    Class Filestorage:
    this class provide ths few methods
    for work whit object, and json files
    return a dictionary from
    instance and file.json

    """
import json
import os

"""
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
"""


class FileStorage:
    """ Class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        a = f'{obj.__class__.__name__}.{getattr(obj, "id")}'
        self.__objects[a] = obj

    def save(self):
        dic = {}
        for key, value in self.__objects.items():
            dic[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dic, f)

    def reload(self):
        """ return list of instan*ce from json file"""

        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as h:
                dictionary = json.load(h)
                for key, value in dictionary.items():
                    obj_class = value['__class__']
                    obj_instance = eval(obj_class + "(**value)")
                    FileStorage.__objects[key] = obj_instance
        else:
            pass
