#!/usr/bin/python3
import json
import os

class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects[f'{obj.__class__.__name__}.{getattr(obj, "id")}'] = obj.__dict__.copy()

    
    def save(self):
        if len(self.__objects) > 0:
            with open(self.__file_path, "w") as file:
                file.write(json.dumps(self.__objects))
        else:
            pass

    def reload(self):
        """ return list of instance from json file"""
        if not os.path.exists(self.__file_path):
            return
        json.load(self.__file_path)
