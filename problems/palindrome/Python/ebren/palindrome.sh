#!/bin/bash

# Check if an argument was provided
if [ $# -eq 0 ]; then
    echo "No arguments provided"
    exit 1
fi

# Run the Python program with the provided argument
python3 "$(dirname "$0")/palindromeCheck.py" "$1"