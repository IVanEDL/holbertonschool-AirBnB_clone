#!/usr/bin/python3

import unittest

from models.place import Place
import models

class Place_TestCase(unittest.TestCase):
    """testing for the class AMenity"""

    def test_type(self):
        a = Place()
        self.assertEqual(type(a.name), str)
        self.assertEqual(type(a.user_id), str)
        self.assertEqual(type(a.city_id), str)
        self.assertEqual(type(a.number_rooms), int)
        self.assertEqual(type(a.number_bathrooms), int)
        self.assertEqual(type(a.max_guest), int)
        self.assertEqual(type(a.price_by_night), int)
        self.assertEqual(type(a.latitude), float)
        self.assertEqual(type(a.longitude), float)
        self.assertEqual(type(a.amenity_ids), list)
        self.assertEqual(type(a.description), str)

    def test_public_attribute(self):
        b = Place()
        b.name = "Martin"
        b.user_id = "12345"
        b.city_id = "12"
        b.description = "verynice"
        b.number_rooms = 2
        b.number_bathrooms = 2
        b.max_guest = 1
        b.price_by_night = 222
        b.latitude = 1.3
        b.longitude = 1.1
        b.amenity_ids = ["12", "12"]
        self.assertEqual(b.name, "Martin")
        self.assertEqual(b.user_id, "12345")
        self.assertEqual(b.city_id, "12")
        self.assertEqual(b.description, "verynice")
        self.assertEqual(b.number_rooms, 2)
        self.assertEqual(b.number_bathrooms, 2)
        self.assertEqual(b.max_guest, 1)
        self.assertEqual(b.price_by_night, 222)
        self.assertEqual(b.latitude, 1.3)
        self.assertEqual(b.longitude, 1.1)
        self.assertEqual(b.amenity_ids, ["12", "12"])


    def test_instan(self):
        a = Place()
        self.assertIsInstance(a, type(Place()))

    def testi_same_object(self):
        a = Place()
        b = Place()
        self.assertIsNot(a, b)

    def test_new_instace_stored(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_attribute_in(self):
        a = Place()
        self.assertNotIn("name", a.__dict__)
        self.assertNotIn("city_id", a.__dict__)
        self.assertNotIn("user_id", a.__dict__)
        self.assertNotIn("description", a.__dict__)
        self.assertNotIn("number_rooms", a.__dict__)
        self.assertNotIn("number_bathrooms", a.__dict__)
        self.assertNotIn("max_guest", a.__dict__)
        self.assertNotIn("price_by_night", a.__dict__)
        self.assertNotIn("latitude", a.__dict__)
        self.assertNotIn("longitude", a.__dict__)
        self.assertNotIn("amenity_ids", a.__dict__)
