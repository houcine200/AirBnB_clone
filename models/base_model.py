#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime




class BaseModel():
    def __init__(self, *args, **kwargs):
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                    if key != "__class__":
                        if key in ["created_at", "updated_at"]:
                            setattr(self, key, datetime.fromisoformat(value))
                        else:
                            setattr(self, key, value)
                    
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        storage.save()
        
    def to_dict(self): 
        from models import storage                                                      
        my_dict = {}
        my_dict["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                my_dict[key] = val.isoformat()
            else:
                my_dict[key] = val
        return my_dict
