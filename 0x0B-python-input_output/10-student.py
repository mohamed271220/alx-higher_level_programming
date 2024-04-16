#!/usr/bin/python3
"""student"""


class Student:
    """student"""
    def __init__(self, first_name, last_name, age):
        """student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """student"""
        try:
            for a in attrs:
                if type(a) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict
