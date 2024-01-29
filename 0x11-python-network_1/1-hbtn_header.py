#!/usr/bin/python3

"""Take in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""

import sys
from urllib.request import urlopen

with urlopen(sys.argv[1]) as response:
    headers = response.info()
    print(headers["X-Request-Id"])
