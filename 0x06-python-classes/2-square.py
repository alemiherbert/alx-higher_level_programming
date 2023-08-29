#!/usr/bin/python3

"""
A simple square lives here
"""


class Square:
    """
    A simple square
    """
    def __init__(self, size=0):
        """
        Initialisation of the simple square

        Args:
            size (int): the length of the side

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
