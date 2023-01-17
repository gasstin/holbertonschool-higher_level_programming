#!/usr/bin/python3
"""
    Python script that fetches
    https://intranet.hbtn.io/status
"""

if __name__ == "__main__":
    from urllib import request
    url = "https://intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        body = response
        text_body = body.read()
    print("Body response:")
    print(f"\t- type: {type(body.read())}")
    print(f"\t- content: {text_body}")
    print(f"\t- utf8 content: {body.msg}")
