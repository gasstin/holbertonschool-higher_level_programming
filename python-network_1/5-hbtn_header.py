#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable found
    in the header of the response.

    You must use the packages requests and sys
"""


if __name__ == "__main__":
    from requests import request
    from sys import argv

    with request(url=argv[1], method='GET') as response:
        print(response['X-Request-Id'])
