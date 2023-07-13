#!/usr/bin/python3
"""Module append write"""


def append_write(filename="", text=""):
    """appends text to a file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
