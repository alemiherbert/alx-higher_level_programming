#!/usr/bin/python3

"""Lets do some numbers!!!"""


class BaseGeometry:
    """ Class that does alot of nothing"""

    def area(self):
        """Calculate the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        Args:
            name (string): the name
            value (int): value

        Raises:
            TypeError: if value is not an integer
            Value Error if value is less than or equal to 0
        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle object"""

    def __init__(self, width, height):
        """Initialise rectangle"""

        self.integer_validator(width)
        self.__width = width
        self.integer_validator(height)
        self.__height = height
