#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5
    add_result = add(a, b)
    subtract_result = sub(a, b)
    multiply_result = mul(a, b)
    divide_result = div(a, b)

    print("{} + {} = {}".format(a, b, add_result))
    print("{} - {} = {}".format(a, b, subtract_result))
    print("{} * {} = {}".format(a, b, multiply_result))
    print("{} / {} = {}".format(a, b, divide_result))


if __name__ == "__main__":
    main()
