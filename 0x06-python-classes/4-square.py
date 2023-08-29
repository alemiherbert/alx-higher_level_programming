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

    def area(self):
        """
        Calculate the area of the square

        Returns: The area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Retrieve the size of the square

        Returns: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square

        Raises:
            ValueError: if value is less than 0
        """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be an integer")
        self.__size = value
