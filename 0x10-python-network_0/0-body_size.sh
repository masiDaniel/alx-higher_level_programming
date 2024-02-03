#!/bin/bash
# size of the response body
curl -sD - "$1" | grep "Content-Length" | cut -d " " -f 2-