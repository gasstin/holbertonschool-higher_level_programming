#!/usr/bin/python3
"""
    Write a Python script that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


if __name__ == "__main__":
    from requests import get, post
    from sys import argv

    req = post('http://0.0.0.0:5000/search_user', data={'q': argv[1]})
    try:
        req_json = req.json()
        if not req_json:
            print('No result')
        else:
            print(f"[{req_json['id']}] {req_json['name']}")
    except:
        print('Not a valid JSON')
