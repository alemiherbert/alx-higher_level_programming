#!/usr/bin/python3

"""Take in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""

import sys
from urllib.request import urlopen, Request

if __name__ == "__main__":
    with urlopen(Request(sys.argv[1])) as response:
        headers = response.info()
        print(dict(headers).get("X-Request-Id"))
