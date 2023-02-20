#!/usr/bin/python3
from add_0 import add as add

if __name__ == "__main__":
    a = 1
    b = 2
    print("{a} + {b} = {add}".format(a=a, b=b, add=add(a, b)))
