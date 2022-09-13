#!/usr/bin/python3

def safe_print_integer(value):
    """
    prints list of anything but only prints int
    returns amount printed
    """
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
