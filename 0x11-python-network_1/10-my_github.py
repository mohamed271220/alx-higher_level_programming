#!/usr/bin/python3
"""
Module to use GitHub API to display user id using Basic Authentication with a personal access token.
"""

import requests
import sys

if __name__ ==  "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    
    url = f"https://api.github.com/user"
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/json'
    }
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        print(data.get('id'))
    except requests.exceptions.RequestException as e:
        print(None)
