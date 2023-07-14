#!/usr/bin/python3
"""square class module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """suare class"""

    def __init__(self, size):
        """initialization"""
        self.integer_validator('size', size)
        super().__init__(size, size)
