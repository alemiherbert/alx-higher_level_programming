#!/usr/bin/python3

"""Send a POST request to a server with a letter as a parameter"""
import sys
import requests


def search_user(letter):
    """Searches for a user by a letter"""
    url = "http://0.0.0.0:5000/search_user"
    params = {'q': letter}

    response = requests.post(url, params=params)
    try:
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    search_user(letter)
