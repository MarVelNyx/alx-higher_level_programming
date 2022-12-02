#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 08:37 2022

@author: Kim Kunniah
"""


BaseGeometry = __import__('7-base-geometry')


class Rectangle(BaseGeometry):
    """
    A Rectangle class shape, inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
