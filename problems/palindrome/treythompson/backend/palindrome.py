import sys

def isPalindrome(arg):
    if(not isinstance(arg, str)):
        return "ERROR: Argument is not a String"
    
    reversedString = arg[::-1]
    if (reversedString == arg):
        return "This is a Palindrome"
    return "NOT a Palindrome"

def main():

    if (len(sys.argv) != 2):
        print("Usage: ./runPalindromeCheck.sh <your string>")
        return

    print(isPalindrome(sys.argv[1]))

main()