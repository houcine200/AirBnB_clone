#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel():
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        
    def to_dict(self):                                                       
        my_dict = {}
        my_dict["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                my_dict[key] = val.isoformat()
            else:
                my_dict[key] = val
        return my_dict
