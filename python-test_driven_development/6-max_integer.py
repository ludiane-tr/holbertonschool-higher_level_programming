#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

def add_integer(a, b=98):
    """Function to add two integers
        If b is not provided, it defaults to 98
    """
    return a + b

def say_my_name(first_name, last_name=""):
    """Function to print a name
        If last_name is not provided, it defaults to an empty string
    """
    print("My name is {} {}".format(first_name, last_name))

def print_square(size):
    """Function to print a square with the character #
        The size of the square is determined by the size parameter
    """
    for i in range(size):
        print("#" * size)

def text_indentation(text):
    """Function to print text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    print(text)

print(add_integer(2, 3))
print(say_my_name("John", "Smith"))
