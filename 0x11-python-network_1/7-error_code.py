#!/usr/bin/python3
""" sends request to url"""

import sys
import requests


def main():
    """ main function"""
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)


if __name__ == "__main__":
    main()
