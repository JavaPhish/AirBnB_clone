#!/usr/bin/python3
""" Base model for data stuff """


import uuid
from datetime import datetime


class BaseModel:
    """ Base model class """

    def __init__(self):
        """ initial stuff """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Prints formatted string about current class """
        cls_name = self.__class__.__name__
        """ Stupid 80 char line limit... UGH """
        return ("[{}] ({}) {}".format(cls_name, self.id, self.__dict__))

    def to_dict(self):
        """ Prep for JSON serial and de-serialization """
        n_dict = self.__dict__
        cls_name = self.__class__.__name__

        n_dict['__class__'] = cls_name
        n_dict['created_at'] = self.created_at.isoformat()
        n_dict['updated_at'] = self.updated_at.isoformat()

        return (n_dict)

    def save(self):
        """ Currently just updates the updated at time """
        self.updated_at = datetime.now()
