import sys

#a function to check if a number is prime
def isPrime(checkMe):
    if(checkMe < 2):
        return False
    for i in range(2, int(checkMe/2)+1):
        if(checkMe % i) == 0:
            return False
            break
    else:
        return True

def main():
    #collect user input 
    userNum =  5
    #int(sys.argv[1])
    #iterate all numbers that lead up to user input
    newNum = 0
    totalSum = 0
    while(newNum < userNum):
        #check if number is prime
        #if number is prime, add it to totalSum (the sum of primes)
        if(isPrime(newNum)):
            totalSum = totalSum+newNum
        newNum = newNum+1
    #print the sum of primes
    #print("The sum of primes up to" , userNum , "is" , totalSum)
    
main()

