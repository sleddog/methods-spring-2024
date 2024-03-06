using System;

namespace FizzBuzz {
  class Program {
    static void Main(string[] args) {
        if(args.Length > 0){

            int num = Convert.ToInt32(args[0]);
            for(int i = 1; i <= num; i++){
                if(i % 3 == 0){
                    Console.Write("Fizz");
                }
                if(i % 5 == 0){
                    Console.Write("Buzz");
                }
                if(i % 3 != 0 && i % 5 != 0){
                    Console.Write(i);
                }
                Console.WriteLine("");
            }
        }
        else{
            Console.WriteLine("No arguments given");
        }
    }
  }
}
