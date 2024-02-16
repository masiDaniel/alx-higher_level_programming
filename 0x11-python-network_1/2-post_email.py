#!/usr/bin/python3
"""script that sends a post request"""

import sys
import urllib.request
import urllib.parse


def main():
    """ main function"""
    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email': email}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
    print(page.decode('utf-8'))


if __name__ == "__main__":
    main()
