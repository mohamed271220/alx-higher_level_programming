#!/usr/bin/python3
"""Module for inherits_from function"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited from the
    specified class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
