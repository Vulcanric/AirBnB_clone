#!/usr/bin/python3
"""
This module defines the `Amenity`'s class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class Amenity:
        This model defines amenity instances

        Every amenity object has the following properties:
        Attributes:
            `name (string)`: Amenity's name. E.g electricity
    """
    name = ''
