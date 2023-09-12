#!/usr/bin/python3

"""Defines a rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle object"""

    def __init__(self, width, height):
        """Initialise rectangle"""

        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle
        Args:
            width (int): the width
            height (int): the height

        Returns:
            the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Return the string representation of a rectangle"""
        return ("[{}] {}/{}".format(str(self.__class__.__name__),
                                    str(self.__width),
                                    str(self.__height)))
