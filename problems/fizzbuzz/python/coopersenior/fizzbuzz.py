import sys

def fizzBuzz(n):
    printStream = ""
    for num in range(1, n + 1):
        if (num > 1):
            printStream = printStream + "\n"
        if num % 3 == 0:
            printStream = printStream + "Fizz"
        if num % 5 == 0:
            printStream = printStream + "Buzz"
        if num % 5 != 0 and num % 3 != 0:
            printStream = printStream + str(num)

    return printStream

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please use the format './run.sh n'")
        sys.exit(1)
    n = int(sys.argv[1])
    print(fizzBuzz(n))
