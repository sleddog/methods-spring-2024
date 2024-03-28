import sys

def getValue(n):
    if n % 5 == 0 and n % 3 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0: 
        return "Buzz"
    return str(n)

def fizzBuzz(n):
    printStream = ""
    for num in range(1, n + 1):
        printStream += getValue(num) + '\n'
    return printStream

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please use the format './run.sh n'")
        sys.exit(1)
    n = int(sys.argv[1])
    print(fizzBuzz(n))
