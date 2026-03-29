#!/usr/bin/python3
"""
This module provides a function for text indentation.
It prints text with two new lines after each '.', '?', and ':'.
It also ensures no spaces exist at the start or end of each line.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The string to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    # Skip leading spaces at the very beginning of the text
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            # Skip spaces following a delimiter or a newline
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
