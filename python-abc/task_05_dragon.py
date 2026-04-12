#!/usr/bin/env python3
"""
Module demonstrating the use of Mixins to compose behaviors in Python.
"""


class SwimMixin:
    """
    A mixin class that provides swimming functionality.
    """

    def swim(self):
        """Prints swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class that provides flying functionality.
    """

    def fly(self):
        """Prints flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that composes behaviors by inheriting from both
    SwimMixin and FlyMixin.
    """

    def roar(self):
        """Prints roaring behavior."""
        print("The dragon roars!")
