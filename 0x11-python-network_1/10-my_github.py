#!/usr/bin/python3
""" displays my github id"""

import sys
import requests
from requests.auth import HTTPBasicAuth


def main():
    """ main function"""
    username = sys.argv[1]
    password = sys.argv[2]
    payload = {'login': sys.argv[1]}
    r = requests.get('https://api.github.com/user',
                     params=payload, auth=(username, password))
    try:
        print(r.json()['id'])
    except KeyError:
        print('None')


if __name__ == "__main__":
    main()
