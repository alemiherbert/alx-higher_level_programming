#!/usr/bin/python3


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
        if type(size) != "int":
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
