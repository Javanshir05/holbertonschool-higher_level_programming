#!/usr/bin/python3
"""
This module defines a Square class.
It demonstrates defining a class with a private instance attribute.
"""


class Square:
    """
    Defines a square by its size.

    Attributes:
        __size (int): Private size of the square.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
