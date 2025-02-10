#!/usr/bin/python3
'''
Function that writes a string to a text file and return the len
'''


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8).
    Returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        Defaults to an empty string.
        text (str): The string to write to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(text)
    return len(text)
