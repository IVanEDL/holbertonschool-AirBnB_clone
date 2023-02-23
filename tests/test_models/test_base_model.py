#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import datetime
class TestBaseModel(unittest.TestCase):

 
    def test_id(self):
          b = BaseModel()
          b1 = BaseModel()
          self.assertNotEqual(b.id, b1.id)

 
    def test_dict(self):
        r1 = BaseModel()
        r1_dictionary = r1.to_dict()
        self.assertEqual(isinstance(r1_dictionary, dict), True)
        self.assertEqual(str(type(r1_dictionary)), "<class 'dict'>")

    def test_to_save(self):
         upd = BaseModel()
         b = upd.updated_at
         upd.save()
         c = upd.updated_at
         self.assertNotEqual(b, c)

    def test_created_at(self):
        ud = BaseModel()
        b = datetime.datetime.now()
        c = ud.created_at
        self.assertNotEqual(c, b)  
         

    
