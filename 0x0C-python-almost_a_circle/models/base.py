#!/usr/bin/python3
"""

The model with the base class for managing ids of
all classes that inherit it.
"""


class Base:
    """
    the base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        nothing special
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
