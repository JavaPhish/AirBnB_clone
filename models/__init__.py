#!/usr/bin/python3
""" Links basemodel and engine thing """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
