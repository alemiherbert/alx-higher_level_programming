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
