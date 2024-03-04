#include <iostream>
#include <stdexcept>
#include <stdlib.h>
using namespace std;
//enter number at end of run command to get input
void error(string in1){
	throw runtime_error("Error: "+in1);
}
int main(int argc, char** argv){
	if(argc<2){
		error("No input");
	}
	int i=atoi(argv[1]);
	for(int k=1; k<=i; k++){
		if(k%3==0 && k%5==0){
			cout<<"FizzBuzz"<<"\n";
		}else if(k%3==0){
			cout<<"Fizz"<<"\n";
		}else if(k%5==0){
			cout<<"Buzz"<<"\n";	
		}else{
			cout<<k<<"\n";	
		}
	}
	return(0);
}
