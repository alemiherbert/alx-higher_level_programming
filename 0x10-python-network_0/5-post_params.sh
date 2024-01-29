#!/bin/bash
# Take in a URL as an argument, send a GET request to the URL, and display the body of the response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
