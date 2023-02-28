#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

import os


class TestFileStorage(unittest.TestCase):
    """ testing for FileStorage"""

    def test_save(self):
        s_test = BaseModel()
        s_test.save()
        self.assertEqual(os.path.exists("file.json"), True)

    def test_json(self):
        """Check file json"""
        with open("file.json") as f:
            self.assertGreater(len(f.read()), 0)

if __name__ == "__main__":
    unittest.main()
