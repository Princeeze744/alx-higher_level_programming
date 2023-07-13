#!/usr/bin/python3
"""Module write file"""


def write_file(filename="", text=""):
    """writes text to file, filename"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
