#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 12:19 2022

@author: Kim Kunniah
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
