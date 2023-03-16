
#include "iostream"
#include "string"
using namespace std;

int main(){
    string name;
    int score;
    string grade;
    cout << "Enter a name and score:" << endl;
    cin >> name;
    cin >> score;

    if( 89< score && score <= 100 ) grade = 'A';
    if( 79< score && score <= 89 ) grade = 'B';
    if( 69< score && score <= 79 ) grade = 'C';
    if( 59< score && score <= 69 ) grade = 'D';
            else grade = 'F'

    cout << "Hi " << name << "! Your grade is "
}
