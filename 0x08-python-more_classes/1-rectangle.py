#!/usr/bin/python3
"""Module contains Rectangle class"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance

        Args:
            width(int): width of the Rectangle instance defaults to 0
            height(int): height of the Rectangle instance defaults to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter method
            Return: width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method.
            Args:
                value(int): sets the width of Rectangle instance
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter method
            Return: height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method.
            Args:
                value(int): sets the height of Rectangele instance
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
