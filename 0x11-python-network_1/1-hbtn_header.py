#!/usr/bin/python3
"""Takes in a URL sends a request"""

import urllib.request
import sys


def main():
    """ main function"""
    url = str(sys.argv[1])
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header = response.headers
        print(header['X-Request-Id'])


if __name__ == "__main__":
    main()
