#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""

import requests


def main():
    """ main function"""
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))


if __name__ == "__main__":
    main()
