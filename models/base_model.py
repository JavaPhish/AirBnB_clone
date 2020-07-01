#!/usr/bin/python3
""" Base model for data stuff """


import uuid
from datetime import datetime
import copy


class BaseModel:
    """ Base model class """

    def __init__(self, *args, **kwargs):
        """ initial stuff """
        from models import storage
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())

        if (kwargs is not None and len(kwargs) is not 0):
            self.id = kwargs['id']

            for key, value in kwargs.items():
                if "__class__" not in key:
                    exec("self.{} = value".format(key))

            form = '%Y-%m-%dT%H:%M:%S.%f'
            self.created_at = datetime.strptime(kwargs['created_at'], form)
            self.updated_at = datetime.now()

    def __str__(self):
        """ Prints formatted string about current class """
        cls_name = self.__class__.__name__
        """ Stupid 80 char line limit... UGH """
        return ("[{}] ({}) {}".format(cls_name, self.id, self.__dict__))

    def to_dict(self):
        """ Prep for JSON serial and de-serialization """

        s_copy = copy.deepcopy(self)
        n_dict = s_copy.__dict__

        n_dict['__class__'] = self.__class__.__name__
        n_dict['created_at'] = self.created_at.isoformat()
        n_dict['updated_at'] = self.updated_at.isoformat()

        return (n_dict)

    def save(self):
        """ Currently just updates the updated at time """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()
