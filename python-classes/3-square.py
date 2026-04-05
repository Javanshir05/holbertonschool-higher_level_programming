#!/usr/bin/python3
"""
This module defines a Square class.
It features private attribute validation and a public area method.
"""


class Square:
    """
    Defines a square by its size.

    Attributes:
        __size (int): Private size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
