#!/usr/bin/python3
"""
Module to send a POST request with an email as a parameter to a given URL
and display the body of the response (decoded in utf-8).
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode("utf-8")
    req = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode("utf-8"))
