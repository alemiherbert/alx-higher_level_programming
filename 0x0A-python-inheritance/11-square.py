#!/usr/bin/python3

"""Defines a rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square object"""

    def __init__(self, size):
        """Initialise a square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
