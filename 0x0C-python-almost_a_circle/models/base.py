#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat 10 Dec 2022 10:21

@author: Kim
"""
import json


class Base:
    """
    Class Base

    Attributes:
        nb_objects (int): Private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor

        Attributes:
            id (int): An integer input for id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns json strin representation

        Attribute:
            list_dictionaries (json): inputted list of dictionaries
        Return:
            json representation
        """
        if list_dictionaries is None or not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the json string reresentation list object to file

        Attribute:
            list_objs (list): object list to save

        Return:
            json object to save in file
        """
        file_name = cls.__name__ + ".json"
        string = []
        if list_objs is not None:
            for i in list_objs:
                string.append(cls.to_dictionary(i))
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(string))
