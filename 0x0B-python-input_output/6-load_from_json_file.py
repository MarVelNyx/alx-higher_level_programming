#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 06 09:28 2022

@author: Kim Kunniah
"""
import json


def load_from_json_file(filename):
    """
    Loads on object from json file

    Arguments:
        filename (str): The name of the output file

    Return:
        A file with a text in json format
    """
    with open(filename, encoding='utf-8') as file:
        return (json.loads(file.read()))
