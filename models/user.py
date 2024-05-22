#!/usr/bin/python3
"""
manages the User class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """manages user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
