#!/usr/bin/python3
"""base geometry module"""


class BaseGeometry():
    """geometry class"""

    def area(self):
        """area public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator public instance method"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
