#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)

- The email must be sent in the email variable
- You must use the packages urllib and sys
- You are not allowed to import packages other than urllib and sys
- You don't need to check arguments passed to the script (number or type)
- You must use the `with` statement

"""

import sys
import urllib.request
import urllib.parse


def send_post_request(url, email):
    """Encode the email parameter"""
    data = urllib.parse.urlencode({"email": email}).encode("ascii")

    with urllib.request.urlopen(url, data=data) as response:
        content = response.read().decode("utf-8")
        print("Response Body:")
        print(content)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    send_post_request(url, email)
