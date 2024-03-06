#!/usr/bin/python3
"""
This module contains the definition of the `City` class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class City:
        This model is used to define city instances

        Every city object has the following characteristics(attribute)
        Attribute:
            `state_id (string)`: is equivalent to State.id. Foreign key to
                identify the state a city is located.
            `name (string)`
    """
    state_id = ''
    name = ''
