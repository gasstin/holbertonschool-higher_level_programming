#!/usr/bin/python3
"""
    Python script that fetches
    https://intranet.hbtn.io/status
"""

if __name__ == "__main__":
    from urllib import request
    url = "https://intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        print("Body response:")
        print(f"\t- type: {type(response.read())}")
        print(f"\t- content: {response.read()}")
        print(f"\t- utf8 content: {response.msg}")
