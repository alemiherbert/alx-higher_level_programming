#!/usr/bin/python3
"""Take in a URL,
- send a request to the URL and 
- display the body of the response (decoded in utf-8).
"""

import sys
from urllib import error, request

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code:", e.code)
