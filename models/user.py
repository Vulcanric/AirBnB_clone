"""
This module contains the definition of the `User` subclass
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User:
        This model is used to define user instances.

        Every user object created from this model has the following attributes:
        Attributes:
            `email (string)`: User's email
            `password (string)`: User's password
            `first_name (string)`: User's first name
            `last_name (string)`: User's last name
    """
    first_name, last_name = '', ''
    email, password = '', ''
