// Java Program to compute the sum of all prime numbers from 2 to a given integer. Note that 0 and 1 are not considered prime numbers.
import static org.junit.Assert.assertEquals;
import org.junit.Test;
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

        @Test
        public static void test10() {
                int sum1 = sumOfPrimes.primeSum(10);
                assertEquals(sum1, 17);
                System.out.println("Test 10 passed");
        }
        
        @Test
        public static void test50() {
                int sum2 = sumOfPrimes.primeSum(50);
                assertEquals(sum2, 328);
                System.out.println("Test 50 passed");
        }

        @Test
        public static void test100() {
                int sum3 = sumOfPrimes.primeSum(100);
                assertEquals(sum3, 1060);
                System.out.println("Test 100 passed");
        }

        @Test
        public static void failedTest100() {
                int sum4 = sumOfPrimes.primeSum(100);
                assertEquals(sum4, 1059);
        }

        public static void main(String[] args) {
                int sumNumber = Integer.parseInt(args[0]);
                System.out.println("The sum of prime numbers between 0 and " + sumNumber + " is " + primeSum(sumNumber));

                test10();
                test50();
                test100();
                failedTest100();
        }
}
