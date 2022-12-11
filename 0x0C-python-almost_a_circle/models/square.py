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
