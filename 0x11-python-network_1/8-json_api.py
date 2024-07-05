#!/usr/bin/python3
"""
Module to send a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    try:
        response = requests.post(url, data={'q': q})
        data = response.json()

        if data:
            print(f"[{data.get('id')}] {data.get('name')}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
    except Exception as e:
        print(e)
