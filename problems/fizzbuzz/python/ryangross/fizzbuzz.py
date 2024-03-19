import sys

def fizzbuzz(n):
    val = "0"
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            val = "FizzBuzz"
            print('FizzBuzz')
            # return val

        elif i % 3 == 0:
            val = "Fizz"
            print('Fizz')
            # return val

        elif i % 5 == 0:
            val = "Buzz"
            print('Buzz')
            # return val

        else:
            val = str(i)
            print(i)
            # return val
    
    # print(val)
    return val
    
        # val is for testing 

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        fizzbuzz(n)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
