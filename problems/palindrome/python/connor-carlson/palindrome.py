import sys

inp = " ".join(sys.argv[1:])
# print(inp)


def isPalendrome(inp:str, lower:int, upper:int):
    while not inp[lower].isalnum():
        lower += 1
    while not inp[upper].isalnum():
        upper -= 1

    if upper > lower:
        if inp[lower] == inp[upper]:
            return isPalendrome(inp, lower+1, upper-1)
        else:
            return False
    else:
        return True
    
def checkInput(inp:str):
    temp = inp.lower()
    if isPalendrome(temp, 0, len(temp)-1):
        print("\"%s\" is a paledrome!" % inp)
    else:
        print("\"%s\" is NOT a plendrome!" % inp)

checkInput(inp)