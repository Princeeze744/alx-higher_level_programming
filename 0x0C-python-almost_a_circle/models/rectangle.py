#!/usr/bin/python3
"""trangle module"""
from models.base import Base


class Rectangle(Base):
    """Triangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializer method"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """returns the area of the given rectangle"""
        return self.width * self.height

    def display(self):
        """displays to stdout the rectangle instance with character '#'"""
        print('\n' * self.y, end='')
        for i in range(self.height):
            print(' ' * self.x, end='')
            for j in range(self.width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        """Updates the rectangle instance"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) == 5:
                self.y = args[4]
        if not args:
            for key in kwargs.keys():
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Returns the dictionary rep of a rectangle instance"""
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}

    def __str__(self):
        """String representation of a rectangle instance"""
        return '[{}] ({}) {}/{} - {}/{}'.format(self.__class__.__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)
