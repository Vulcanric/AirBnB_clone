#!/usr/bin/python3
"""
This module contains the definition of the `State` class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class State:
        This model is used to define state instances

        Every state defined has the following attribute
        Attributes:
            `name (string)`: Name of the state
    """
    name = ''
