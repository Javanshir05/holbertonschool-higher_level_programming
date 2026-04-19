#!/usr/bin/python3
"""
Module for basic JSON serialization and deserialization.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file into a Python dictionary.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
