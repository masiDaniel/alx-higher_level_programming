#!/usr/bin/python3
"""Uses the GitHub API to display GitHub commits"""

import sys
import requests
from requests.auth import HTTPBasicAuth


def main():
    repo, owner = sys.argv[1], sys.argv[2]
    hdr = {"Accept": "application/vnd.github.v3+json"}
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    r = requests.get(url, headers=hdr)
    [print("{}: {}".format(cmit["sha"], cmit["commit"]["author"]["name"]))
     for cmit in r.json()[0:10]]


if __name__ == "__main__":
    main()
