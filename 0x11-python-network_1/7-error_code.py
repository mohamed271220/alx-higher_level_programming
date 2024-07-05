#!/usr/bin/python3
"""
Module to send a request to a given URL and display the body of the response.
If the HTTP status code is >= 400, print the error code.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
