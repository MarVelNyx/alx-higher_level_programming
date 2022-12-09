#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri 09 Dec 2022 13:23

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

    def to_json(self):
        """
        Represents of Student into json format

        Return:
            Student class as a json format
        """
        return {key: value for (key, value) in self.__dict__.items()
                if key in list(self.__dict__.keys())}
