public class tests
{

    public static boolean check(String s)
    {
        return PalindromeCheck.isPalindrome(s);
    }

    public static void main(String[] args)
    {
        System.out.println("Is 'racecar' a palindrome?: " + check("racecar"));
        System.out.println("Is 'A man, a plan, a canal, Panama!' a palindrome?: " + check("A man, a plan, a canal, Panama!"));
        System.out.println("Is 'apple' a palindrome?: " + check("apple"));
        System.out.println("Is 'Hello World!' a palindrome?: " + check("Hello World!"));
        System.out.println("Is '12344321' a palindrome?: " + check("12344321"));
        System.out.println("Is 'AbbA' a palindrome?: " + check("AbbA"));
        System.out.println("Is 'ABABABA' a palindrome?: " + check("ABABABA"));
        System.out.println("Is 'OoOO' a palindrome?: " + check("OoOO"));
        System.out.println("Is 'E!G#ge' a palindrome?: " + check("E!G#ge"));
    }
}