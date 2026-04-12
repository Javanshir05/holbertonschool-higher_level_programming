#!/usr/bin/env python3
"""
Module defining an abstract Shape class, its subclasses Circle and Rectangle,
and a function demonstrating duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract Base Class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Subclass representing a Circle shape.
    """

    def __init__(self, radius):
        """
        Initializes a Circle with a given radius.
        Uses absolute value to handle potential negative radius inputs.
        """
        self.radius = abs(radius)

    def area(self):
        """
        Calculates the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculates the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Subclass representing a Rectangle shape.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with a given width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape relying entirely on duck typing.
    Does not explicitly check if `shape` is a subclass of `Shape`.
    
    Args:
        shape (any): An object that is expected to have `area` and `perimeter` methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
