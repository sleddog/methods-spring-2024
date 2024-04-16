# Palindrome Checker

This is a simple web application built with Flask that checks if a given string is a palindrome.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python and Flask installed on your machine. You can install Flask with pip:

\```bash
pip install flask
\```

### Running the Application

To run the application, navigate to the directory containing the `palindrome.py` file and run:

\```bash
python palindrome.py
\```

The application will start on your local machine, usually on port 5000. You can access it by navigating to `http://localhost:5000` in your web browser.

## Using the Application

The application has two routes:

- `/` : This route renders the `index.html` file.
- `/check-palindrome` : This route accepts a POST request with a JSON body containing a 'palindrome' key. The value of this key is the string that you want to check. The route will return "true" if the string is a palindrome, "false" if it is not, and "Invalid input" if the input is not valid.
