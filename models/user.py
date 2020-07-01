#!/usr/bin/python3
""" User data, inherits base """


from models import storage
from models.base_model import BaseModel


class User(BaseModel):
    """ see head """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
