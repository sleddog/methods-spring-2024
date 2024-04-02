import sys


def isPalindrome(word):
    if word == "":
        return True
    for i in range(0, int(len(word)/2)):
        if word[i] != word[len(word)-i-1]:
            return False
        else:
            return True

def main():
    inputString = sys.argv[1]
    
    if (isPalindrome(inputString)):
        print("The string " + inputString + " is a palindrome!")
    else:
        print("The string " + inputString + " is NOT a palindrome!")
        

main()