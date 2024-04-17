# Methods 2024 Trey Thompson Palindrome Solution

## Introduction

This repository contains a solution to determine whether a given string is a palindrome or not. The solution includes an HTML document presenting the solution and instructions on how to use it, along with a Python script that performs the palindrome check.

The Python script runPalindromeCheck.py contains the logic for determining whether a given string is a palindrome. It defines a function isPalindrome(arg) that takes a string argument and returns whether it is a palindrome or not.

To run the script, execute it from the command line with the string you want to check as an argument.

```bash
./runPalindromeCheck.py 'your string'
```

There is a unit test for the palindrome function. The tests will ensure that the palindrome function returns the correct result and when it returns an argument error.

## NodeJS documentation for assignment 6:

This is a simple Node.js application that checks whether a given string is a palindrome or not. It provides a web interface where users can input a string, and the application will return whether the string is a palindrome or not.

## Installation
Before running the application, you need to make sure you have Node.js and npm installed on your system.
Once you have Node.js and npm installed, you need to install the required dependencies. Run the following command in your terminal:

```bash
npm install
```
This will install the necessary packages, then install express:

```bash
npm install express
```

## Usage
To start the application, run the following command:

```bash
node app.js
```

This will start the server, and you should see a message indicating that the server is listening at a specific port (by default, port 3000).

Once the server is running, you can access the web interface by opening a web browser and navigating to http://localhost:3000. Enter a string in the provided input field and submit the form. The application will then return whether the string is a palindrome or not.