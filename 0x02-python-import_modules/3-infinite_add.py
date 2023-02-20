#!/usr/bin/python3
from sys import argv as argv

if __name__ == "__main__":
    somme = 0
    for arg in range(1, len(argv)):
        somme += int(argv[arg])
    print(f"{somme}")
