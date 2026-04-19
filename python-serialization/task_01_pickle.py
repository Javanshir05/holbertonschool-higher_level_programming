#!/usr/bin/python3
"""
Module for serializing and deserializing custom Python objects using pickle.
"""
import pickle


class CustomObject:
    """A custom class representing a person."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in a formatted way."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance and saves it to a file.

        Args:
            filename (str): The name of the file to save the object to.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads an instance of CustomObject from a file.

        Args:
            filename (str): The name of the file to load the object from.

        Returns:
            CustomObject: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            
            # Ensure the loaded object is actually an instance of this class
            if not isinstance(obj, cls):
                return None
            return obj
        except (FileNotFoundError, EOFError, pickle.UnpicklingError, OSError):
            return None
