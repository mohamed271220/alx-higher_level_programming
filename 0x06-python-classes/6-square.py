#!/usr/bin/python3
"""This is a module that defines a square."""


class Square:
    """This is a class that defines a square with
    private instance attributes size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """This is the constructor method that initializes
        the size and position of the square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """This is a method to get the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """This is a method to set the size.
        The size must be an integer and greater than or equal
         to 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """This is a method to get the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """This is a method to set the position.
        The position must be a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This is a method that returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """This is a method that prints in stdout the square
        with the character #."""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join(" " * self.__position[0] + "#" * self.__size 
                            for _ in range(self.__size)))