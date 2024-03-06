public class PalindromeCheck {
    public static boolean isPalindrome(String text) 
    {
        String stringInput = text.replaceAll("[^A-za-z]+", "").toLowerCase(); //lowercases the input, special characters and spaces are gone
        int length = stringInput.length(); //get length of modified string
        int forward = 0; //iterate forward
        int back = length - 1; //iterate backwards

        while(back > forward)
        {
            char forwardChar = stringInput.charAt(forward++); //first character in string 
            char backChar = stringInput.charAt(back--); //last character in string

            if(forwardChar != backChar)
            {
                return false; //return false if characters in string dont match, therefore it's not a palindrome
            }
            return true; //exit the loop and return true
        }
        return true; //return value to make isPalindrome() work in main
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