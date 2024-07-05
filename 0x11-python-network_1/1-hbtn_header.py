#!/usr/bin/python3
"""
Module to fetch and display the X-Request-Id header value from a URL
using urllib and sys.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.info()
        print(header.get("X-Request-Id"))
