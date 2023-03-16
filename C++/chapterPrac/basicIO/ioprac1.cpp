#include <iostream>
using namespace std;
int main(){
    int sum=0;
    for(int i =1 ; i < 6; i++){
        int inputData;
        cout << i << "번째 정수입력 : " ;
        cin >> inputData;
        sum += inputData;
    }
    cout << "합계 : " << sum << endl;
    return 0;
}