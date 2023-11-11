#!/usr/bin/python3
"""
User class that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    define User classe that
    inherits from BaseModel class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
