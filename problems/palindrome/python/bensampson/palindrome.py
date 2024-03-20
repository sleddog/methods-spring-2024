import sys

inputString = "racecar"

def isPalindrome(word):
    if word == "":
        return True
    for i in range(0, int(len(word)/2)):
        if word[i] != word[len(word)-i-1]:
            print("The string " + word + " is NOT a palindrome!")
            return False
        else:
            print("The string " + word + " is a palindrome!")
            return True

def main():
    
    if (isPalindrome(inputString)):
        print("The string " + inputString + " is a palindrome!")
    else:
        print("The string " + inputString + " is NOT a palindrome!")
        

isPalindrome(inputString)