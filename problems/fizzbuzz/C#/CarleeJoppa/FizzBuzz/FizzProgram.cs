using System;

namespace FizzBuzzSol {
  public class FizzBuzzProgram {

    public static string FizzBuzz(int highest){
        string output = null;
        for(int i = 1; i <= highest; i++){
            if(i % 3 == 0 && i % 5 == 0){
                output += "<p>FizzBuzz</p>";
            }
            else{
                if(i % 3 == 0){
                    output += "<p>Fizz</p>";
                }
                if(i % 5 == 0){
                    output += "<p>Buzz</p>";
                }
                if(i % 3 != 0 && i % 5 != 0){
                    output += "<p>" + i.ToString() + "</p>" ;
                }
            }
        }

        return output;
    }
    static void Main(string[] args) {
        if(args.Length > 0){

            int num = Convert.ToInt32(args[0]);
            string output = FizzBuzz(num);
        
        }
        else{
            Console.WriteLine("No arguments given");
        }
    }
  }
}