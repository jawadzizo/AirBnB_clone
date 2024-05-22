#!/usr/bin/python3
"""
manages the Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """manages review objects"""

    place_id = ""
    user_id = ""
    text = ""
