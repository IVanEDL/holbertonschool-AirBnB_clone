#!/usr/bin/python3

""" Basic testing"""

import unittest

from models.state import State
import models

class State_TestCase(unittest.TestCase):
    """testing for the class State"""

    def test_type(self):
        a = State()
        self.assertEqual(type(a.name), str)

    def test_public_attribute(self):
        b = State()
        b.name = "Martin"
        self.assertEqual(b.name, "Martin")

    def test_instance(self):
        a = State()
        self.assertIsInstance(a, type(State()))

    def testi_same_object(self):
        a = State()
        b = State()
        self.assertIsNot(a, b)

    def test_new_instace_stored(self):
        self.assertIn(State(), models.storage.all().values())

    def test_attribute_in(self):
        a = State()
        self.assertNotIn("name", a.__dict__)
