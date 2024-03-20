import sys

def uniqueString(string: str) -> bool:
    if len(set(string)) == len(string):
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(uniqueString(sys.argv[1]))