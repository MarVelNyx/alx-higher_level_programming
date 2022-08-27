#!/usr/bin/python3

def element_at(my_list, idx):
    """
    gets an element in list at given index
    and returns it
    """
    if idx >= len(my_list) or idx < 0:
        return

    return (my_list[idx])
