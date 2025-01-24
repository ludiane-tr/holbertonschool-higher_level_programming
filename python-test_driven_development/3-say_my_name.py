#!/usr/bin/python3
"""
    To define a function that prints "My name is <first name> <last name>"
"""

# Project Title

This is a sample project to demonstrate code corrections and formatting.

## Description

This project includes several Python scripts and tests.

### Usage

To use the scripts, run the following commands:

```sh
python3 0-main.py
python3 3-main.py
```

def say_my_name(first_name, last_name=""):
    """
    Print "My name is <first name> <last name>"

    Args:
        first_name (str): The first name.
        last_name (str): The last name.

    Raise:
        TypeError: if first_name and last_name are not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")

print(add_integer(2, 3))
