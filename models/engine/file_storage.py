#!/usr/bin/python3
""" JSON storage handler """


import os.path
import json
import copy
from models.base_model import BaseModel
from models.user import User
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.city import City

class FileStorage:
    """ Filestorage class """

    """ Path the the storage file """
    __file_path = 'file.json'

    """ This will store objects be <class name>.id """
    __objects = {}

    def all(self):
        """ Returns all objects by id (__objects) """
        return FileStorage.__objects

    def new(self, obj):
        """ adds a new id into __objects """
        k_name = "{}.{}".format(str(obj.__class__.__name__), obj.id)

        FileStorage.__objects[k_name] = obj.to_dict()

    def save(self):
        """ Save all current data to a json file """
        with open(FileStorage.__file_path, 'w') as j_file:
            json.dump(FileStorage.__objects, j_file)

    def reload(self):
        """ Loads all data from the json file """
        if (os.path.isfile(self.__file_path) is True):
            with open(self.__file_path, 'r') as j_data:
                FileStorage.__objects = json.load(j_data)
