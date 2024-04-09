# Alex Ellingsen's Unique Char Solution

This function takes any string as an input and returns "True" or "False" depending on if there are any repeated characters in the string.

To run the script, use the command **./run.sh**, with a string following the command. The string can be comprised of any characters.

If there are any errors running the shell script, try changing "python" in run.sh to "python3".

### Running the backend
To run the backend, first make sure flask is installed. Then, run the program **backend.py**, and click on the IP address listed. This will bring you to a webpage where you can use the form to enter a string of characters, and will return true if is is completely
unique, or false if not.

### Unit Tests
To preform unit tests, use the command **./test.sh**. This runs 3 tests that will confirm that the program functions with all types of characters/