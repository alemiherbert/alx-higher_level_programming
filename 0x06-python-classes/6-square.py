#!/usr/bin/python3

"""
A simple square lives here
"""


class Square:
    """
    A simple square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialisation of the simple square

        Args:
            size (int): the length of the side
            position (tuple): where to print the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple) or len(position) != 2 or \
                any(i < 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """
        Retrieve the position

        Returns:
            The position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of a square

        Args:
            value: the position of the square
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Print a square using the # symbol
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
