#!/usr/bin/python3
"""Text indentation module"""


def text_indentation(text):
    """prints 2 new lines after every '.', '?' and ':' character in text"""
    if type(text) is not str:
        raise TypeError('text must be a string')
    for i, char in enumerate(text):
        if not char.isspace():
            indent = False
        if char in ('.', '?', ':'):
            indent = True
            print(f'{char}\n')
            continue
        if char.isspace() and indent:
            continue
        print(char, end='')
