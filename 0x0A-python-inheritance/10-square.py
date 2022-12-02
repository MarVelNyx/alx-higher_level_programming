#!/usr/bin/python3
# -*- coding: uft-8 -*-
"""
Created on Fri Dec 02 09:08 2022

@author: Kim Kunniah
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square class ahpe, inherits from Rectangle and BaseGeometry
    """
    def __init__(self, size):
        """
        Init function for Square

        Attributes:
            size (int): The size of the square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculates area of the square

        Return:
            the area of the square
        """
        return self.__size ** 2
