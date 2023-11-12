#!/usr/bin/python3
"""Unit tests for the FileStorage class."""
import json
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for the methods in the FileStorage class."""

    def setUp(self):
        """Set up the necessary components for testing."""
        super().setUp()
        self.file_path = storage._FileStorage__file_path
        self.instance = BaseModel()
        self._objs = storage._FileStorage__objects
        self.keyname = "BaseModel." + self.instance.id

    def tearDown(self):
        """Clean up by removing the test file if it exists."""
        super().tearDown()
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_methods(self):
        """Test if essential methods exist in the FileStorage class."""
        object = FileStorage
        self.assertTrue(hasattr(object, "all"))
        self.assertTrue(hasattr(object, "new"))
        self.assertTrue(hasattr(object, "save"))
        self.assertTrue(hasattr(object, "reload"))

    def test_all_method(self):
        """Test the 'all()' method to ensure it returns the correct objects."""
        rslt = storage.all()
        self.assertEqual(rslt, self._objs)

    def test_new_method(self):
        """Test the 'new()' method to verify correct addition of objects."""
        storage.new(self.instance)
        key = "{}.{}".format(self.instance.__class__.__name__, self.instance.id)
        self.assertIn(key, self._objs)

    def test_save_method(self):
        """Test the 'save()' method to confirm proper data saving."""
        my_model = BaseModel()
        my_model.name = "My_New_Model"
        my_model.my_number = 98
        storage.new(my_model)
        storage.save()
        with open(self.file_path, "r") as dt_file:
            saved_data = json.load(dt_file)

        expected_data = {}
        for key, val in self._objs.items():
            expected_data[key] = val.to_dict()

        self.assertEqual(saved_data, expected_data)

    def test_reload_method(self):
        """Test the 'reload()' method to ensure correct reloading of data."""
        my_model = BaseModel()
        my_model.name = "My_New_Model"
        my_model.my_number = 98
        storage.new(my_model)
        storage.save()
        with open(self.file_path, 'r') as f:
            saved_data = json.load(f)
        storage.reload()

        with open(self.file_path, 'r') as f:
            reloaded_data = json.load(f)

        self._objs = {}
        self.assertEqual(reloaded_data[self.keyname], saved_data[self.keyname])

    def test_path(self):
        """Test the existence of the JSON file."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.assertFalse(os.path.exists(self.file_path))
        storage.reload()


if __name__ == "__main__":
    unittest.main()
