#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """
    BaseModel class.

    It provides ID generation, timestamping, string representation,
    saving to storage, and conversion to dictionary.

    Attributes:
    - id (str): Unique identifier for each instance.
    - created_at (datetime): Timestamp indicating the creation time.
    - updated_at (datetime): Timestamp indicating the last update time.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of BaseModel.

        If provided with kwargs, populate instance attributes from kwargs.
        Otherwise, generate a new ID, set creation and update timestamps,
        and add the instance to storage.

        Args:
        - *args: Variable length argument list.
        - **kwargs: Arbitrary keyword arguments.
        """
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
        """
        Save the instance to storage and update the 'updated_at' timestamp.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Convert the instance to a dictionary.

        Returns:
        - dict: Dictionary representation of the instance.
        """
        from models import storage
        my_dict = {}
        my_dict["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                my_dict[key] = val.isoformat()
            else:
                my_dict[key] = val
        return my_dict
