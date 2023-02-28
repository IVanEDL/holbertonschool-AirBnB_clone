#!/usr/bin/python3
from models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self):
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 1
        self.number_bathrooms = 1
        self.max_guest = 1
        self.price_by_night = 1
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
