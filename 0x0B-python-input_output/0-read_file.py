#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """function reads a text file and prints it to stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
