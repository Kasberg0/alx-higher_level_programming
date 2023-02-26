#!/usr/bin/python3
from calculator_1 import add, mul, sub, div

if __name__ == "__main__":
    a = 10
    b = 5
    print("{a} + {b} = {add}".format(a=a, b=b, add=add(a, b)))
    print("{a} - {b} = {add}".format(a=a, b=b, add=sub(a, b)))
    print("{a} * {b} = {add}".format(a=a, b=b, add=mul(a, b)))
    print("{a} / {b} = {add}".format(a=a, b=b, add=div(a, b)))
