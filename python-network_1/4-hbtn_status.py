#!/usr/bin/python3
"""
    Write a Python script that fetches https://intranet.hbtn.io/status

    You must use the package requests
"""


if __name__ == "__main__":
    from requests import request

    url = "https://intranet.hbtn.io/status"

    with request(url=url, method='GET') as response:
        print("Body response:")
        print(f"\t- type: {type(response._content.decode('utf8'))}")
        print(f"\t- content: {response._content.decode('utf8')}")
