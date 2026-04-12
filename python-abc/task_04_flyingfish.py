#!/usr/bin/env python3
"""
Module demonstrating multiple inheritance with Fish, Bird, and FlyingFish classes.
"""


class Fish:
    """
    A class representing a Fish.
    """

    def swim(self):
        """Prints swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """
    A class representing a Bird.
    """

    def fly(self):
        """Prints flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Prints the habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a FlyingFish, inheriting from both Fish and Bird.
    """

    def fly(self):
        """Prints flying behavior of a flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints swimming behavior of a flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints the habitat of a flying fish."""
        print("The flying fish lives both in water and the sky!")
