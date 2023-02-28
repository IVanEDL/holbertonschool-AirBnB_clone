#!/usr/bin/python3

from models.base_model import BaseModel
from uuid import uuid4

class User(BaseModel):
    "Inherits from BAseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __init__(self):
        self.id = BaseModel().id
