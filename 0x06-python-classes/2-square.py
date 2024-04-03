#!/usr/bin/python3
"""This is a module that defines a square."""


class Square:
    """This is a class that defines a square
     with a private instance attribute size."""

    def __init__(self, size=0):
        """This is the constructor method that
        initializes the size of the square.
        The size must be an integer and
        greater than or equal to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
