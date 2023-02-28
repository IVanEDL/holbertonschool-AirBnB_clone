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
class FileStorage:
    """ Class """
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects[f'{obj.__class__.__name__}.{getattr(obj, "id")}'] = obj

    
    def save(self):
        dic = {}
        if len(self.__objects) > 0:
            for key, value in self.__objects.items():
                try:
                    dic[key] = value.to_dict()
                except Exception:
                    dic[key] = value
            with open(self.__file_path, "w") as f:
                json.dump(dic, f)
        else:
            pass

    def reload(self):
        """ return list of instan*ce from json file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as h:
                self.__objects = json.load(h)
        else:
            pass
