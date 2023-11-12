#!/usr/bin/python3
"""
Module to manage storage for hbnb clone
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """
    FileStorage class to manage storage for hbnb clone
    """

    # Class attributes
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        dict_obj = {}
        for key, val in FileStorage.__objects.items():
            dict_obj[key] = val.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf_8") as jfile:
            json.dump(dict_obj, jfile)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing)
        """
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, "r") as file:
                dict_to_obj = json.load(file)
            for key, val in dict_to_obj.items():
                FileStorage.__objects[key] = eval(val["__class__"] + '(**val)')
        except FileNotFoundError:
            pass
