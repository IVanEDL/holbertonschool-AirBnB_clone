#!/usr/bin/python3
import unittest
from models.review import Review
import models

import os


class TestReview(unittest.TestCase):
    """ testing for the class Review"""

    def test_attr_type(self):
        a = Review()
        self.assertEqual(type(a.place_id), str)
        self.assertEqual(type(a.user_id), str)
        self.assertEqual(type(a.text), str)

    def test_public_attr(self):
        a = Review()
        a.place_id = "martinasfadfadfadfav4357657"
        a.user_id = "42536tegdrfg53e6tgq35q4"
        a.text = "how are you?"
        self.assertEqual(a.place_id, "martinasfadfadfadfav4357657")
        self.assertEqual(a.user_id, "42536tegdrfg53e6tgq35q4")
        self.assertEqual(a.text, "how are you?")
     
    def test_attr(self):
        a = Review()
        self.assertNotIn("place_id", a.__dict__)
        self.assertNotIn("user_id", a.__dict__) 
        self.assertNotIn("text", a.__dict__)
    
    def test_instance(self):
        a = Review()
        self.assertIsInstance(a, type(Review()))
