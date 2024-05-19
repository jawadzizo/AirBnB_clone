#!/usr/bin/python3
""" Module of the BaseModel class to be used as parent class for other classes
"""

from datetime import datetime
from models import storage
import uuid


class BaseModel():
    """The base class of other subclasses"""

    def __init__(self, *args, **kwargs):
        """
        initiates the instance with the attributes id, created_at and
        updated_at
        """

        if len(kwargs) != 0:
            self.id = kwargs['id']
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            self.created_at = datetime.strptime(kwargs['created_at'],
                                                date_format)
            self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                date_format)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        """
        returns a formated instance object as:
        [<class name>] (<self.id>) <self.__dict__>
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the "updated_at" attribute with the current time
        """

        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary of the instance attribtes, with also:
        - key __class__: the name of the instance class
        - updates the "created_at" and "updated_at" keys to use isoformat
        """

        instance_attributes = self.__dict__.copy()
        instance_attributes["created_at"] = self.created_at.isoformat()
        instance_attributes["updated_at"] = self.updated_at.isoformat()
        instance_attributes["__class__"] = self.__class__.__name__

        return (instance_attributes)
