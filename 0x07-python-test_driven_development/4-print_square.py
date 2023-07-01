#!/usr/bin/python3
"""Print square module"""


def print_square(size):
    """Prints a square with character #"""
    if type(size) is not int or type(size) is float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
