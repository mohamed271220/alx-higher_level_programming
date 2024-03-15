#!/usr/bin/python3
from sys import argv


def main():
    sum = 0
    for arg in argv[1:]:
        sum += int(arg)
    print(sum)


if __name__ == "__main__":
    main()
