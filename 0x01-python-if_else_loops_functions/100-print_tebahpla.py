#!/usr/bin/python3
print("".join([chr(i - 32) if i % 2 == 1 else chr(i) for i in range(122, 96, -1)]), end="")
