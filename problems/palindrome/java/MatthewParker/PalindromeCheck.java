public abstract class PalindromeCheck {
    public static boolean isPalindrome(String text) 
    {
        String stringInput = text.replaceAll("[^A-za-z]+", "").toLowerCase(); //lowercases the input, special characters and spaces are gone
        
        int i = 0, j = stringInput.length() - 1;

        while(i < j)
        {
            if (stringInput.charAt(i) != stringInput.charAt(j))
            {
                return false;
            }

            i++;
            j--;
        }

        return true;

    }

    public static void main(String[] args)
    {
        String s = ""; //blank string

        for(String i : args) //turn .sh args into a string
        {
            s += i;
        }

        if(!isPalindrome(s)) //check if isPalindrome() returned false
        {
            System.out.println("Your input is not a palindrome.");
        }

        else //return true by default
        {
            System.out.println("Your input is a palindrome.");
        }
    }
}