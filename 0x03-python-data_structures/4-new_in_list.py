#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    replaces element in list at specific index
    without modifying original list
    """
    if idx >= len(my_list) or idx < 0:
        return (my_list)
    new_list = my_list.copy()
    new_list[idx] = element
    return (new_list)
