#!/usr/bin/python3
"""
    Write a Python script that takes your GitHub credentials
    (username and password) and uses the GitHub API to display your id
"""


if __name__ == "__main__":
    from requests import get, post, exceptions
    from sys import argv

    req = get('https://api.github.com/user', auth=(argv[1], argv[2]))
    if req.status_code == 200:
        print(req.json()['id'])
    else:
        print(None)
