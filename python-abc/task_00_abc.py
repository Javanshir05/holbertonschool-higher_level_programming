#!/usr/bin/env python3
"""
Module defining an Animal abstract base class and its subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract Base Class representing an Animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    Subclass of Animal representing a Dog.
    """

    def sound(self):
        """
        Returns the sound made by a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Subclass of Animal representing a Cat.
    """

    def sound(self):
        """
        Returns the sound made by a cat.
        """
        return "Meow"
