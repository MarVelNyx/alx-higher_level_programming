#!/usr/bin/python3

import sys

if __name__ != "__main__":
    exit()

i = 0
result = 0
for argu in sys.argv:
    if i != 0:
        result += int(argu)
    else:
        i += 1
print("{:d}".format(result))
