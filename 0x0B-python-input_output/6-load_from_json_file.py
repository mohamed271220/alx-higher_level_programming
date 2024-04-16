#!/usr/bin/python3
"""Load from json file"""


import json


def load_from_json_file(filename):
    """Load from json file"""
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
