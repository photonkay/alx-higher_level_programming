#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import urllib.request
import sys

# if len(sys.argv) != 2:
#     print("Usage: {} <URL>".format(sys.argv[0]))
#     sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
except urllib.error.HTTPError as e:
    print("Error:", e)
    sys.exit(1)
