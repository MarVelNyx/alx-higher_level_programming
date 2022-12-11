#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun 11 Dec 2022 10:05

@author: Kim
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor for Square

        Attributes:
            size (int): size of square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str___(self):
        """
        str method for class square

        Return:
            string: [class_name] (id) x/y - size
        """
        string = "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                               self.id, self.x, self.y,
                                               self.size)
        return string

    def update(self, *args, **kwargs):
        """
        Updates square class

        Attributes:
            args (list): inputted argments to update square class
            kwargs (dict): inputted arguments to update square class
        """
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        elif kwargs is not None and len(kwargs) != 0:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    @property
    def size(self):
        """
        Property method for size value

        Return:
            Private value size value
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter method for size value

        Attribute:
            value (int): value to check if int and greater than 0
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
