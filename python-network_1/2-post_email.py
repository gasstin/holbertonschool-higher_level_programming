#!/usr/bin/python3
"""
    Python script that takes in a URL and an email,
    sends a POST request to the passed URL
    with the email as a parameter,
    and displays the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    url = argv[1]
    new_data = {'email': argv[2]}

    data = parse.urlencode(new_data).encode('utf8')
    new_request = request.Request(url, data)
    with request.urlopen(new_request) as response:
        print(response.read().decode('utf8'))