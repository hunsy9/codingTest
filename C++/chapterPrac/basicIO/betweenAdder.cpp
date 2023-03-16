#include <iostream>

int main(){
    int val1,val2;

    std::cout << "두 개의 숫자를 입력해주세요." << std::endl;
    std::cin >> val1 >> val2;

    int sum=0;
    if(val1 < val2){
        for (int i=1; i<val2-val1; i++){
            sum+=(val1+i);
        }
    }
    else{
        for(int i = val2+1; i<val1; i++){
            sum+=i;
        }
    }
    std::cout << "두 숫자 사이 값들의 합은: " << sum << std::endl;


    return 0;
}