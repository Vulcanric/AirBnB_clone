#!/usr/bin/python3
"""This file contains definition of the BaseModel class and all its methods"""
import uuid
from datetime import datetime


class BaseModel:
    """
    The Base class, defines all common methods and attributes for other
    classes. Such methods/attributes includes:

    Common Attributes
        * `id` (string):
                Universally unique identifier attached to objects.
        * `created_at` (datetime):
                Assigns with the current datetime when an instance is created
        * `updated_at` (datetime):
                Assigns with the current datetime when an instance is created
                and it will be updated every time an object is changed.
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiate a new model:
        Create a new model or recreate an existing model via its dictionary
        """
        # Recreate an existing one using kwargs
        if kwargs:
            for attr, value in kwargs.items():
                if attr == "__class__":
                    pass
                elif attr in ['created_at', 'updated_at']:
                    setattr(self, attr, datetime.fromisoformat(value))
                else:
                    setattr(self, attr, value)
        # Create a new one
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return an informal representation of a model/object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save the object and update its time to the current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of this object/model.
        The dictionary contains all its(object's) attributes with their names
        """
        object_dict = self.__dict__.copy()

        # Change the datetime object to strings according to ISO format
        object_dict["created_at"] = self.created_at.isoformat()
        object_dict["updated_at"] = self.updated_at.isoformat()
        object_dict = {'__class__': self.__class__.__name__, **object_dict}
        return object_dict
