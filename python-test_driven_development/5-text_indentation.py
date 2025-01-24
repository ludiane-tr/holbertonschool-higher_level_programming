#!/usr/bin/python3
"""
    Define that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be processed.

    Raise:
        TypeError: if the text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    result = ""
    while i < len(text):
        result += text[i]
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
    print(result, end="")

def add_integer(a, b=98):
    """
    Add two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer, default is 98.

    Returns:
        int: The sum of a and b.

    Raise:
        TypeError: if a or b are not integers.
    """
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b