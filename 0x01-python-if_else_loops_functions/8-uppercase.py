#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            result += "{:c}".format(ord(char) - 32)
        else:
            result += "{:c}".format(ord(char))
    print(result)
