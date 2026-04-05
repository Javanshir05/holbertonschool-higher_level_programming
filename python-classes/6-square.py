#!/usr/bin/python3
"""
This module defines a Square class.
It features size and position properties, area calculations,
and prints a visual square shifted by position coordinates.
"""


class Square:
    """
    Defines a square by its size and position.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): A tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Computes the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the '#' character to stdout.
        Shifts the output vertically and horizontally based on position.
        """
        if self.__size == 0:
            print("")
            return

        # Print vertical spacing
        for _ in range(self.__position[1]):
            print("")

        # Print the square rows
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
