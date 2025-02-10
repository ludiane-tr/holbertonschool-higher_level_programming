#!/usr/bin/python3
'''
Function that reads a text file (UTF8) and prints it to stdout
'''


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to be read.
        Defaults to an empty string.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
