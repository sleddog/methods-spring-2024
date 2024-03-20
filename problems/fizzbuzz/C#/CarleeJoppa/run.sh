#!/bin/sh

userInput="$1"

csc .\FizzBuzzSolution\FizzBuzz\Program.cs

./Program.exe "$userInput"
