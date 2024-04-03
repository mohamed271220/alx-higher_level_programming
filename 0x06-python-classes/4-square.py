#!/usr/bin/python3


class Square:
    """This is a class that defines a square with a private instance attribute size."""

    def __init__(self, size=0):
        """This is the constructor method that initializes the size of the square."""
        self.size = size

    @property
    def size(self):
        """This is a method to get the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """This is a method to set the size.
        The size must be an integer and greater than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This is a method that returns the current square area."""
        return self.__size ** 2
