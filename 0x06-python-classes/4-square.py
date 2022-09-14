#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:12 2022
@author: Kim Kunniah
"""

class Square:
    """Class Square that has attributes. Instantiation with size

    Attributes:
        size (int): size of square
    """

    def __init__(self, size=0):
        """The __init__ method for Square class

        Args:
            size: (:obj: 'int', optional): prive instance size
        """
        self.__size = size

    @property
    def size(self):
        """Call the function to check property

        Returns:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """checks errors and setter for size attribute

        Args:
            value: value to check srrors

        Raises:
            TypeError: exception if size is not integer
            ValueError: Eception if size < 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square

        Returns:
            the area of the square
        """
        return self.__size ** 2
