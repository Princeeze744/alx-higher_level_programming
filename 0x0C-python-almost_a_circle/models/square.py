#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[{}] ({}) {}/{} - {}'.format(self.__class__.__name__,
                                             self.id, self.x,
                                             self.y, self.size)

    @property
    def size(self):
        """size getter method"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter method"""
        if type(size) is not int:
            raise TypeError('width must be an integer')
        if size < 0:
            raise ValueError('width must be > 0')
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates attributes of the square instance"""
        if not args:
            for key in kwargs.keys():
                setattr(self, key, kwargs[key])
        else:
            self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

    def to_dictionary(self):
        """To dictionary representation"""
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
