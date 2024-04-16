def is_palindrome(s):
    cleanString = ''.join(char.lower() for char in s if char.isalnum())
    if len(cleanString) <= 1:
        return True
    left = 0
    right = len(cleanString) - 1
    while left < right:
        if cleanString[left] != cleanString[right]:
            return False
        left += 1
        right -= 1
    return True


def main():
    import sys
    user_input = sys.argv[1]
    if (is_palindrome(user_input)):
        print(user_input + " is a palindrome")
    else:
        print(user_input + " is not a palindrome")


if __name__ == "__main__":
    main()
