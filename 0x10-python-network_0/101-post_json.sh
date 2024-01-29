#!/bin/bash
# Send a JSON POST request to a given URL with a given JSON File
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
