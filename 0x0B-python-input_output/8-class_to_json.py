#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 06 10:01 2022

@author: Kim Kunniah
"""


def class_to_json(obj):
    """
    Creates a json representation of an object

    Arguments:
        obj (obj): The object inputed to create a class

    Return:
        A json representation
    """
    return {key: value for (key, value) in obj.__dict__.items()
            if key in list(obj.__dict__.keys())}
