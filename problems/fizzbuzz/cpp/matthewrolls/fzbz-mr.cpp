#include <iostream>
#include <stdexcept>
#include <stdlib.h>
#include <string>
#include <cassert>
using namespace std;

string fb(int inp){
	string s;
	for(int k=1; k<=inp; k++){
		if(k%3==0 && k%5==0){
			s.append("FizzBuzz\n");
		}else if(k%3==0){
			s.append("Fizz\n");
		}else if(k%5==0){
			s.append("Buzz\n");	
		}else{
			s.append(to_string(k));
			s.append("\n");	
		}
	}
	return s;
}
int main(int argc, char** argv){
	int i=atoi(argv[1]);
	if(i>0){
		string out = fb(i);
		cout<<out;
	}else{
		cout<<"Testing\n";
		assert("1\n2\nFizz\n"==fb(3));
		cout<<"First test passed\n";
		assert("1\n2\nFizz\n4\nBuzz\n"==fb(5));
		cout<<"Second test passed\n";
		assert("1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n"==fb(15));
		cout<<"Third test passed\n";
	}
	return(0);
}
