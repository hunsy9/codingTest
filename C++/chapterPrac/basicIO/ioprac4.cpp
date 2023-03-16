#include <iostream>

using namespace std;

int main(){
    int val;

    while(true){
        cout << "판매금액을 만원단위로 입력(-1 to end): ";
        cin >> val;

        if(val==-1){
            cout << "프로그램을 종료합니다."<<endl;
            return 0;
        }

        cout << "이번 달 급여 : " << 50 + val * 0.12 << "만원" <<endl;
    }
    return 0;
}