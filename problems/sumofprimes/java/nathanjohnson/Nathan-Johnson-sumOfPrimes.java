// Java Program to compute the sum of all prime numbers from 2 to a given integer. Note that 0 and 1 are not considered prime numbers.

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

        static int primeSum(int sumNumber) {
                int sum = 0;
                for (int i = 2; i <= sumNumber; i++) {
                        boolean isPrime = checkIfPrime(i); // checks if value i is prime
                        if (isPrime) {
                                sum = sum + i; // adds i to prime number sum if i is prime
                        }
                }
                return sum;
        }

        public static void main(String[] args) {
                int sumNumber = Integer.parseInt(args[0]);
                System.out.println("The sum of prime numbers between 0 and " + sumNumber + " is " + primeSum(sumNumber));
        }
}
