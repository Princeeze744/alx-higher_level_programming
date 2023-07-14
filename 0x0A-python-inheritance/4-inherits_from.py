#!/usr/bin/python3
"""inherits from module"""


def inherits_from(obj, a_class):
    """inherits from class"""
    return issubclass(type(obj), a_class) and not type(obj) is a_class
