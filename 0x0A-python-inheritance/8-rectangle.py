#!/usr/bin/python3

"""Defines a rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle object"""

    def __init__(self, width, height):
        """Initialise rectangle"""

        self.integer_validator(width)
        self.__width = width
        self.integer_validator(height)
        self.__height = height
