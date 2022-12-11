#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat 10 Dec 2022 10:40

@author: Kim
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class Constructor for Rectangle

        Attributes:
            width (int): Private attribute for width of Rectangle
            height (int): Private attribute for height of Rectangle
            x (int): Private attribute for x of Rectangle
            y (int): Private attribute for y of Rectangle
            id (int): Private attribute id inherits from Base
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            The area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Prints the # char Rectangle
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """
        str method for class Rectangle

        Return:
            string: [class_name] (id) x/y - width/height
        """
        string = "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                  self.id, self.x, self.y,
                                                  self.width, self.height)
        return string

    def update(self, *args, **kwargs):
        """
        Update rctangle class

        Attribute:
            args (list): inputted arguments to update rectangle class
            kwargs (dict): inputted arguments to update rectangle class
        """
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        elif kwargs is not None and len(kwargs) != 0:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Creates a dictionary representation of rectangle attributes

        Return:
            A dictionary represtation
        """
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height,
                'width': self.width}

    @property
    def width(self):
        """
        Property method for width value

        Return:
            Private value width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method for width value

        Attributes:
            value (int): value to check if int and greater than 0
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        Property method for height value

        Return:
            Private value height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method for height value

        Attribute:
            value (int): value to check if int and greater than 0
        """
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        Property method of x value

        Return:
            Private value x value
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter method for x value

        Attribute:
            value (int): value to check if int and greater than 0
        """
        if type(value) != int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
        Property method for y value

        Return:
            Private value y value
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter method for y value

        Attribute:
            value (int): check if int and greater than 0
        """
        if type(value) != int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
