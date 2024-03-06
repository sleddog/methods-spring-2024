import sys

def palindrome_check(user_string):
	for index in range(len(user_string)//2):
		if user_string[index] != user_string[len(user_string) - index - 1]:
			return False
	return True

def main():
	user_input = sys.argv[1]

	user_input = user_input.lower()
	
	result = palindrome_check(user_input)
	
	if result == True:
		print(f"{user_input} is a palindrome")
	else:
		print(f"{user_input} is not a palindrome")

main()
