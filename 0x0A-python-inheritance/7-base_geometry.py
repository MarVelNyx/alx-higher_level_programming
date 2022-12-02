#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 08:24 2022

@author: Kim Kunniah
"""


class BaseGeometry():
    """
    An empty class
    """
    pass

    def area(self):
        """
        Public instance method that calculates the area

        Raises:
            Exception if area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates integer input
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")