#!/usr/bin/python3
from sys import argv as argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("{arg} arguments.".format(arg=len(argv)-1))
    elif len(argv) == 2:
        print(f"{len(argv)-1} argument:")
        print(f"{len(argv)-1}: {argv[-1]}")
    else:
        print("{arg} arguments:".format(arg=len(argv)-1))
        for i in range(1, len(argv)):
            print("{i}: {argument}".format(i=i, argument=argv[i]))
