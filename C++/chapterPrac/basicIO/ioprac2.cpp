#include <iostream>
using namespace std;
int main(){
    char name[200];
    char phone[300];

    cout << "이름을 입력해주세요: " ;
    cin >> name ;
    cout << "전화번호를 입력해주세요: " ;
    cin >> phone ;

    cout << "이름은 "<< name <<"이고 전화번호는 " << phone << "입니다."<< endl;

}