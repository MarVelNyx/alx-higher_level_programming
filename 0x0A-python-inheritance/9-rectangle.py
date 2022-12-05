#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 08:48 2022

@author: Kim Kunniah
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class shape, inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        init function for Rectangle

        Attributes:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        str function for rectangle

        Returns:
            Returns width/height
        """
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)

    def area(self):
        """
        Calculates the area of the rectangle

        Return:
            The area of the rectangle
        """
        return self.__width * self.__height