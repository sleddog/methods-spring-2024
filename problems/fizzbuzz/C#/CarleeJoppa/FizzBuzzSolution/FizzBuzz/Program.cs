using System;

namespace FizzBuzzSol {
  public class FizzBuzzProgram {

    public static string[] FizzBuzz(int highest){
        string[] output = new string[highest];
        for(int i = 1; i <= highest; i++){
            if(i % 3 == 0 && i % 5 == 0){
                output[i-1] = "FizzBuzz";
            }
            else{
                if(i % 3 == 0){
                    output[i-1] = "Fizz";
                }
                if(i % 5 == 0){
                    output[i-1] = "Buzz";
                }
                if(i % 3 != 0 && i % 5 != 0){
                    output[i-1] = i.ToString();
                }
            }
        }

        return output;
    }
    static void Main(string[] args) {
        if(args.Length > 0){

            int num = Convert.ToInt32(args[0]);
            string[] output = FizzBuzz(num);
            foreach(string nums in output){
                Console.WriteLine(nums);
            }
        }
        else{
            Console.WriteLine("No arguments given");
        }
    }
  }
}
