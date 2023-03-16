#include <iostream>

using namespace std;

struct Client{
    char account;
    char username[30];
    int balance;
};

void make_account(Client user);
void deposit_money(Client user);
void withdraw_money(Client user);
void show_status(Client user);
void caseFunction(int caseNum,Client user);

int main(void)
{
    struct Client user;
    while(true){
        int chosen;
        cout << "------Menu------" << endl;
        cout << "1. 계좌개설" << endl;
        cout << "2. 입 금" << endl;
        cout << "3. 출 금" << endl;
        cout << "4. 계좌정보 전체 출력" << endl;
        cout << "5. 프로그램 종료" << endl;
        cout << "선택: ";
        cin >> chosen;
        caseFunction(chosen,user);
    }
    
    return 0;
}

void make_account(Client user){
    cout << "[계좌개설]" << endl;
    cout << "계좌ID: " ;
    cin >> ;
    cout << "이 름: " ;
    cin >> user.username;
    cout << "입금액: " ;
    cin >> user.balance;

}

void deposit_money(Client user){
    cout << "[계좌개설]" << endl;
    cout << "계좌ID: " ;
    cin >> user.account;
    cout << "입금액: " ;
    cin >> user.balance;
}
void withdraw_money(Client user){
    cout << "[계좌개설]" << endl;
    cout << "계좌ID: " ;
    cin >> user.account;
    cout << "이 름: " ;
    cin >> user.username;
    cout << "입금액: " ;
    cin >> user.balance;
}
void show_status(Client user){
    cout << "[계좌개설]" << endl;
    cout << "계좌ID: " ;
    cin >> user.account;
    cout << "이 름: " ;
    cin >> user.username;
    cout << "입금액: " ;
    cin >> user.balance;
}


void caseFunction(int caseNum,Client user){
    switch (caseNum)
            {
            case 1:
                make_account(user);
                break;
            case 2:
                deposit_money(user);
                break;
            case 3:
                
                break;
            case 4:
                
                break;
            default:
                break;
            }
}