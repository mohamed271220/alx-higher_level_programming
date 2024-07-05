#!/usr/bin/python3
"""
Module to send a request to a given URL and display the value of the
X-Request-Id variable from the response header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
