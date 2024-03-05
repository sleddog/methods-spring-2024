#!/bin/bash

while true; do
    read -p "Enter a string (type 'exit' to quit): " input
    
    if [ "$input" == "exit" ]; then
        echo "Exiting program."
        break
    fi

    # Run the Python program with the provided argument
    python3 "$(dirname "$0")/palindromeCheck.py" "$input"
done
