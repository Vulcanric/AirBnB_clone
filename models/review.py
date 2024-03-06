#!/usr/bin/python3
"""
This module defines the `Review` model
"""
from models.base_model import BaseModel


class review(BaseModel):
    """
    Class Review:
        This model defines reviews instances

        Every review object has the following properties
        Attributes:
            `place_id (string)`: Same as Place.id
                                Id of the place the review was made for.
            `user_id (string)`: Same as User.id
                                Id of the user who made the review.
            `text (string)`: The review text.
    """
    place_id, user_id, text = '', '', ''
