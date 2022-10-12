#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 09:27 2022

@author: Kim Kunniah
"""


class MyList(list):
    """
    class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Public instance method that prints sored list
        """
        list_copy = self[:]
        list_copy.sort()
        print(list_copy)
