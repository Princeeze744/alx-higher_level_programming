#!/usr/bin/python3
"""Module contains function that add 2 numbers"""


def add_integer(a, b=98):
    """Function adds 2 numbers
    Args:
        a(int): first number
        b(int): second number with 98 as default

    Return: int the addition of a and b
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
