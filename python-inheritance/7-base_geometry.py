#!/usr/bin/python3
'''creating a class named BaseGeometry'''


class BaseGeometry:
    """Base class for geometry operations"""

    def area(self):
        """Raise an exception indicating the method is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that 'value' is an integer greater than 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
