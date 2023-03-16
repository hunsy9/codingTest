#include <iostream>

int main(){
    int val1;
    std::cout << "첫번째 숫자입력: ";
    std::cin >> val1;

    int val2;
    std::cout << "두번째 숫자입력: ";
    std::cin >> val2;

    std::cout << "두 숫자의 합은 " << val1+val2 << std::endl;
    return 0;
}