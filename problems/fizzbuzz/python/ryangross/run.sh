#!/bin/bash

# Check if the number of arguments provided is correct
if [ "$#" -ne 1 ]; then
    exit 1
fi

# Check if the argument is a valid integer
if ! [[ $1 =~ ^[0-9]+$ ]]; then
    echo "Error: Invalid input. Please provide a valid integer."
    exit 1
fi

# Run the program with the integer input
# Replace './your_program' with the path to your program
python3 fizzbuzz.py "$1"
