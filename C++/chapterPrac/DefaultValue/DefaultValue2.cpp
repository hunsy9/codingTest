#include <iostream>

using namespace std;
int Adder(int num1=1,int num2=2);


int main(void){
    cout << Adder() <<endl;
    cout << Adder(5) <<endl;
    cout << Adder(3,5) <<endl;

    return 0;
}

int Adder(int num1,int num2)
{
    return num1 + num2;
}