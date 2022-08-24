#!/usr/bin/python3


def uppercase(str):
    for s in str:
        ch = ord(s)
        if ch >= 97 and ch <= 122:
            ch -= 32
        print("{:c}".format(ch), end="")
    print()
