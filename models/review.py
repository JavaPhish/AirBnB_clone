#!/usr/bin/python3
""" City stuff """


from models.base_model import BaseModel


class Review(BaseModel):
    """ Review data """

    place_id = ""
    user_id = ""
    text = ""
