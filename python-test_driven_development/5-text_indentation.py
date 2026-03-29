#!/usr/bin/python3
"""
Module 5-text_indentation
Defines a function that prints text with specific formatting.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The string to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Flag to skip spaces after . ? : or at start of string
    skip_space = True

    for char in text:
        if skip_space and char == ' ':
            continue

        print(char, end="")
        skip_space = False

        if char in ".?:":
            print("\n")
            skip_space = True
