import sys
       
def uniqueChars(str):
    str_set = ""
    for i in str:
        if i not in str_set:
            str_set+=i
    if (str_set == str):
        return True
    else:
        return False
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("To run this program, write './uniquecharacters.sh {input}'")
        sys.exit(1)
    else:
        print(uniqueChars(sys.argv[1]))