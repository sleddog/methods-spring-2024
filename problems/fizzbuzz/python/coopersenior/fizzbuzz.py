import sys

def fizzBuzz(n):
    for num in range(1, n + 1):
        if num % 3 == 0:
            print("Fizz", end="")
        if num % 5 == 0:
            print("Buzz", end="")
        if num % 5 != 0 and num % 3 != 0:
            print(str(num), end="")
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please use the format './run.sh n'")
        sys.exit(1)
    n = int(sys.argv[1])
    fizzBuzz(n)
