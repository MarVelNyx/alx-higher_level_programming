#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    prints list of anything, only prints integer
    returns amount of integers printed
    """
    counter = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            counter += 1
        except:
            continue
        print()
        return counter
