#include <iostream>

using namespace std;

int main(){
    
    char name[300];
    char lang[300];

    cout << "당신의 이름은 무엇입니까? : " << endl;
    cin >> name;

    cout << "당신의 좋아하는 프로그래밍 언어는 무엇입니까? : " << endl;
    cin >> lang; 

    cout << "당신의 이름은 " << name << "입니다." <<endl;
    cout << "당신의 좋아하는 언어는 " << lang << "입니다." <<endl;

    return 0;

}