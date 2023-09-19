#!/usr/bin/python3

"""
Summary: This module contains the rectangle class of the project
Author: Alemi Herbert <alemiherbert@gmail.com>
Created: September 2023
(c) Alemi Herbert 2023
"""

from models.base import Base


class Rectangle(Base):
    """
    The rectangle class
    """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialise the rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)
    
    @width.setter
    def width(self, width):
        self.validate_dim("width", width)
        self.__width = width
    
    @property
    def height(self):
        return (self.__height)
    
    @height.setter
    def height(self, height):
        self.validate_dim("height", height)
        self.__height = height
    
    @property
    def x(self):
        return (self.__x)
    
    @x.setter
    def x(self, x):
        self.validate_pos("x", x)
        self.__x = x
    
    @property
    def y(self):
        return (self.__y)
    
    @y.setter
    def y(self, y):
        self.validate_pos("y", y)
        self.__y = y

    def validate_int(self, name, value):
        """Validate integer values for a rectangle"""
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        return (value)
    

    def validate_dim(self, name, value):
        """Validate dimension values for a rectangle"""
        value = self.validate_int(name, value)
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))
    
    def validate_pos(self, name, value):
        """Validate position values for a rectangle"""
        value = self.validate_int(name, value)
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
    
    def area(self):
        """Calculate the area of a rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """Prints a rectangle of '#'s to stdout"""
        for i in range(self.height):
            for j in range(self.width):
                print("#", end='')
            print()
    
    def __str__(self):
        """Prints the string representation of a rectangle"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")
    
