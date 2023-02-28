#!/usr/bin/python3

import unittest

from models.amenity import Amenity
import models

class Amenity_TestCase(unittest.TestCase):
    """testing for the class AMenity"""

    def test_type(self):
        a = Amenity()
        self.assertEqual(type(a.name), str)

    def test_public_attribute(self):
        b = Amenity()
        b.name = "Martin"
        self.assertEqual(b.name, "Martin")

    def test_instance(self):
        a = Amenity()
        self.assertIsInstance(a, type(Amenity()))

    def testi_same_object(self):
        a = Amenity()
        b = Amenity()
        self.assertIsNot(a, b)

    def test_new_instace_stored(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_attribute_in(self):
        a = Amenity()
        self.assertIn("name", a.__dict__)
