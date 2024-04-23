//package sumprimes2.src.test.java;

import org.junit.Test;

import com.example.sumOfPrimes;

import static org.junit.Assert.*;


public class testSumOfPrimes {
        
        @Test
        public void test10() {
                int sum1 = sumOfPrimes.primeSum(10);
                assertEquals(sum1, 17);
                //System.out.println("Test 10 passed");
        }
        
        @Test
        public void test50() {
                int sum2 = sumOfPrimes.primeSum(50);
                assertEquals(sum2, 328);
                //System.out.println("Test 50 passed");
        }

        @Test
        public void test100() {
                int sum3 = sumOfPrimes.primeSum(100);
                assertEquals(sum3, 1060);
                //System.out.println("Test 100 passed");
        }

        @Test
        public void failedTest100() {
                int sum4 = sumOfPrimes.primeSum(100);
                assertNotEquals(sum4, 1059);
        }
    
}
