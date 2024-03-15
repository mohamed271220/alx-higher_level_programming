#!/usr/bin/python3
from calculator_1 import add, subtract, multiply, divide


def main():
    a = 10
    b = 5
    add_result = add(a, b)
    subtract_result = subtract(a, b)
    multiply_result = multiply(a, b)
    divide_result = divide(a, b)

    print("Add: ", add_result)
    print("Subtract: ", subtract_result)
    print("Multiply: ", multiply_result)
    print("Divide: ", divide_result)


if __name__ == "__main__":
    main()
