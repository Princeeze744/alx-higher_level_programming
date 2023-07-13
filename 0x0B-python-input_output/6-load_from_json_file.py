#!/usr/bin/python3
"""MOdule load_from_json_file"""
import json


def load_from_json_file(filename):
    """Creates an object from JSON file"""
    with open(filename, "r") as file:
        obj = json.load(file)
    return obj
