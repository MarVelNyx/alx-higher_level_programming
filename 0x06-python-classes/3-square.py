#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:05 2022
@author: Kim Kunniah
"""

class Suare:
    """Class Square that has attributes. Instantiation with size

    Attributes:
        size (int): The size of the square
    """

    def __init__(self, size=0):
        """The __init__ method for Square class

        Args:
            size: (:obj: 'int', optional): A private instance size

        Raises:
            TypeError: Exception if size not an integer
            ValueError: Exception if size < 0
        """
        if type(size) is not int:
            raise TypeError("size must be an intger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of square

        Returns:
            the square area
        """
        return self.__size ** 2
