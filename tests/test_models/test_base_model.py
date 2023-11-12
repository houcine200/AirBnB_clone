#!/usr/bin/python3
"""
Unit tests for the BaseModel class in the models module.
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_creation_with_kwargs(self):
        """
        Test case for creating a BaseModel instance with keyword arguments.
        """
        kwargs = {
            "id": "tempo_id",
            "created_at": "2023-02-01T08:30:00",
            "updated_at": "2023-02-02T16:45:00",
            "custom_attribute": "tempo_value"
        }
        instance = BaseModel(**kwargs)

        self.assertEqual(instance.id, "tempo_id")
        self.assertEqual(
            instance.created_at, datetime.fromisoformat("2023-02-01T08:30:00")
            )
        self.assertEqual(
            instance.updated_at, datetime.fromisoformat("2023-02-02T16:45:00")
            )
        self.assertEqual(
            getattr(instance, "custom_attribute", None), "tempo_value"
            )

    def test_creation_without_kwargs(self):
        """
        Test case for creating a BaseModel instance without keyword arguments.
        """
        instance = BaseModel()

        self.assertIsNotNone(instance.id)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """
        Test case to ensure the save method updates the 'updated_at' attribute.
        """
        instance = BaseModel()
        original_updated_at = instance.updated_at

        # Simulate some time passing
        instance.save()

        self.assertNotEqual(instance.updated_at, original_updated_at)

    def test_to_dict_conversion(self):
        """
        Test case for converting a BaseModel instance to a dictionary.
        """
        instance = BaseModel(
            id="tempo_id", created_at="2023-02-01T08:30:00",
            custom_attribute="tempo_value"
            )
        instance_dict = instance.to_dict()

        self.assertEqual(instance_dict["__class__"], "BaseModel")
        self.assertEqual(instance_dict["id"], "tempo_id")
        self.assertEqual(instance_dict["created_at"], "2023-02-01T08:30:00")
        self.assertEqual(instance_dict.get("custom_attribute"), "tempo_value")


if __name__ == '__main__':
    unittest.main()
