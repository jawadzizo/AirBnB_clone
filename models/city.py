#!/usr/bin/python3
"""
manages the City class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """manages city objects"""

    state_id = ""
    name = ""
