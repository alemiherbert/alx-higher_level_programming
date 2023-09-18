#!/usr/bin/python3

"""
Summary: Square class that inherits from Rectangle
Author: Alemi Herbert <alemiherbert@gmail.com>
Created: September 2023
(c) Alemi Herbert 2023
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialise the square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the square"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))
    @property
    def size(self):
        """Getter for size"""
        return (self.width)
    
    @size.setter
    def size(self, value):
        """Setter for size"""
        self.validate_dim("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the square class
        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
