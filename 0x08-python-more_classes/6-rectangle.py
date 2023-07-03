#!/usr/bin/python3
"""Module contains Rectangle class"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance

        Args:
            width(int): width of the Rectangle instance defaults to 0
            height(int): height of the Rectangle instance defaults to 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Area instance method
            Return: area of the calling Rectangle instance.
                    if either height or width is zero area() returns 0
                    as the resulting shape will only be a line
        """
        return self.height * self.width

    def perimeter(self):
        """Perimeter instance method
            Return: perimeter of the calling Rectangle instance.
                    If either height or width is zero perimeter() returns 0
                    as the resulting shape will only be a straight line.
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """Defines '#'printed representation of Rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        rect = []
        for i in range(self.height):
            if i > 0:
                rect.append('\n')
            [rect.append('#') for j in range(self.width)]
        return "".join(rect)

    def __repr__(self):
        """Defines string representation of Rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """prints message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
