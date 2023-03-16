#include <iostream>
using namespace std;
int main(){
    int val;

    cout << "숫자를 입력해주세요: ";
    cin >> val;

    for (int i=1; i<10; i++){
        cout << val << " x " << i << " = " << val * i << endl;
    }

    return 0;
}