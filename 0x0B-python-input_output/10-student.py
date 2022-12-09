#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri 09 Dec 13:44

@author: Kim Kunniah
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        init method for Student class

        Attributes:
            first_name (str): The first name of student
            last_name (str): The last name of student
            age (int): The age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self, attrs=None):
            """
            Represents to Student into json format

            Return:
                Student class as a json format
            """
            if attrs in None:
                return self.__dict__
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
