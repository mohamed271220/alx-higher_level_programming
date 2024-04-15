#!/usr/bin/python3
"""Module for my_list class"""


class MyList(list):
    """Custom list class"""
    def print_sorted(self):
        """Prints the list sorted"""
        print(sorted(self))
