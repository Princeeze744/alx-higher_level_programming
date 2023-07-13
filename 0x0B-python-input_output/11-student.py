#!/usr/bin/python3
"""Module student"""


class Student():
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dict representation of the class"""
        if attrs is not None:
            return {key: val for key, val in self.__dict__.items()
                    if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for attr in json.keys():
            if attr in self.__dict__.keys():
                setattr(self, attr, json[attr])
