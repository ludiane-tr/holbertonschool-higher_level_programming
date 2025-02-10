#!/usr/bin/python3
'''
Function that appends a string
'''


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8).
    Returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        Defaults to an empty string.
        text (str): The string to append to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="UTF-8") as file:
        file.write(text)
    return len(text)
