#!/usr/bin/python3
"""
This module defines a Square class.
It demonstrates defining a class with type and value validation
for its private instance attribute.
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
            size (int): The size of the square (must be an integer >= 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
