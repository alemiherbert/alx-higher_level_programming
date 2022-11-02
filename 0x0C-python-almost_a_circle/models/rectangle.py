#!/usr/bin/python3
"""
This module contains a rectangle class that inherits from Base
"""
from .base import Base


class Rectangle(Base):
    """
    A rectangle class that inherits from base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        ...
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        ...
        """
        return self.__width

    @property
    def height(self):
        """
        ...
        """
        return self.__height

    @property
    def x(self):
        """
        ...
        """
        return self.__x

    @property
    def y(self):
        """
        ...
        """
        return self.__y

    @width.setter(self, val):
        """
        ...
        """
        self.__width = val

    @height.setter(self, val):
        """
        ...
        """
        self.__height = val

    @x.setter(self, val):
        """
        ...
        """
        self.__x = val

    @y.setter(self, val):
        """
        ...
        """
        self.__y = val
