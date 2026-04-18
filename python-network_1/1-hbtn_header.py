#!/usr/bin/python3
"""Sends a request to a URL and displays the X-Request-Id header value"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get('X-Request-Id'))
