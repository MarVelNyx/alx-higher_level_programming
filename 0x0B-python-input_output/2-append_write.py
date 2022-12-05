#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 05 21:27 2022

@author: Kim Kunniah
"""


def append_write(filename="", text=""):
    """
    Appends inputed text into a utf-8 encoded text file

    Arguments:
        filename (str): The name of the file to open
        text (str): The text to append

    Return:
        A file with append text
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
