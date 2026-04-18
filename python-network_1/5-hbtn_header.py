#!/usr/bin/python3
"""Module that sends a request and displays the X-Request-Id header value"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
