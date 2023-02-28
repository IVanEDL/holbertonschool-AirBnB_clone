#!/usr/bin/python3

import unittest

from models.city import City
import models

class City_TestCase(unittest.TestCase):
    """testing for the class AMenity"""

    def test_type(self):
        a = City()
        self.assertEqual(type(a.name), str)
        self.assertEqual(type(a.state_id), str)

    def test_public_attribute(self):
        b = City()
        b.name = "Martin"
        b.state_id = "12345"
        self.assertEqual(b.name, "Martin")
        self.assertEqual(b.state_id, "12345")

    def test_instance(self):
        a = City()
        self.assertIsInstance(a, type(City()))

    def testi_same_object(self):
        a = City()
        b = City()
        self.assertIsNot(a, b)

    def test_new_instace_stored(self):
        self.assertIn(City(), models.storage.all().values())

    def test_attribute_in(self):
        a = City()
        self.assertNotIn("name", a.__dict__)
