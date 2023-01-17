#!/usr/bin/python3
"""
    Python script that takes in a URL,
    sends a request to the URL and
    displays the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    url = argv[1]

    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf8'))
    except error.HTTPError as err:
        print(f"Error code: {str(err)}")
