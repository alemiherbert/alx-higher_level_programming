#!/usr/bin/python3

"""
Summary: This module contains the base class of the project
Author: Alemi Herbert <alemiherbert@gmail.com>
Created: September 2023
(c) Alemi Herbert 2023
"""

import json

class Base:
    """
    The base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialise the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))