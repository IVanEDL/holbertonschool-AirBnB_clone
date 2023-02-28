#!/usr/bin/python3
import unittest
from models.user import User
import models

import os


class TestUser(unittest.TestCase):
    """ testing for the class User"""

    def test_attr_type(self):
        a = User()
        self.assertEqual(type(a.first_name), str)
        self.assertEqual(type(a.last_name), str)
        self.assertEqual(type(a.email), str)
        self.assertEqual(type(a.password), str)
    
    def test_public_attr(self):
        a = User()
        a.first_name = "martin"
        a.last_name = "Correa"
        a.email = "martin@elias.com"
        a.password = "hola"
        self.assertEqual(a.first_name, "martin")
        self.assertEqual(a.last_name, "Correa")
        self.assertEqual(a.email, "martin@elias.com") 
        self.assertEqual(a.password, "hola")
     
    def test_attr(self):
        a = User()
        self.assertNotIn("first_name", a.__dict__)
        self.assertNotIn("last_name", a.__dict__) 
        self.assertNotIn("email", a.__dict__)
        self.assertNotIn("password", a.__dict__)
    
    def test_instance(self):
        a = User()
        self.assertIsInstance(a, type(User()))
