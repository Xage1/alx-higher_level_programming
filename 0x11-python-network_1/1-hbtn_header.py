#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL, and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    # Check if URL is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            # Check if the 'X-Request-Id' header is present in the response
            if 'X-Request-Id' in response.headers:
                x_request_id = response.headers['X-Request-Id']
                print(x_request_id)
            else:
                print("X-Request-Id header not found in the response.")
    except urllib.error.URLError as e:
        print("Error:", e.reason)
