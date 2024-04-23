package com.example;

public class sumOfPrimes {

    static boolean checkIfPrime(int value) {
        if(value < 2) {
                return false;
        }
        for (int i = 2; i*2 <= value; i++) {
                if (value % i == 0) {
                        return false;
                }
        }
        return true;
    }

    public static int primeSum(int sumNumber) {
        int sum = 0;
        for (int i = 2; i <= sumNumber; i++) {
                boolean isPrime = checkIfPrime(i); // checks if value i is prime
                if (isPrime) {
                        sum = sum + i; // adds i to prime number sum if i is prime
                }
        }
        return sum;
    }

}
