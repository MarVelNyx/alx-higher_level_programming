#!/usr/bin/python3

def multiple_returns(sentence):
    """
    returns tuple with length of string and its first
    character
    """
    s_len = len(sentence)
    if s_len == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return ((s_len, first_char))
