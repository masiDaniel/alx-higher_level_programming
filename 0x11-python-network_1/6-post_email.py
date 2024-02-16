#!/usr/bin/python3
""" sends a POST request to url"""

import sys
import requests


def main():
    """ main function"""
    url = str(sys.argv[1])
    email = str(sys.argv[2])
    r = requests.post(url, data={'email': email})
    print(r.text)


if __name__ == "__main__":
    main()
