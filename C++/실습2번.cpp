//
// Created by 유승훈 on 2023/03/15.
//

#include "iostream"
#include "string"
#include "limits"

using namespace std;

int printRange(string str){
    if(str=="int") {
        cout << numeric_limits<int>::min() << "   " << numeric_limits<int>::max() << endl;
        return 0;
    }
    if(str=="long") {
        cout << numeric_limits<long>::min() << "   " << numeric_limits<long>::max() << endl;
        return 1;
    }
    if(str=="float") {
        cout << numeric_limits<float>::min() << "   " << numeric_limits<float>::max() << endl;
        return 2;
    }
    if(str=="double") {
        cout << numeric_limits<double>::min() << "   " << numeric_limits<double>::max() << endl;
        return 3;
    }
    if(str=="char") {
        cout << numeric_limits<char>::min() << "   " << numeric_limits<char>::max() << endl;
        return 4;
    }
}

void printQuit(int memoryArr[]){
    cout << "=== A List of # of types ===" << endl;
    cout << "int:" << memoryArr[0] << endl;
    cout << "long:" << memoryArr[1] << endl;
    cout << "float:" << memoryArr[2] << endl;
    cout << "double:" << memoryArr[3] << endl;
    cout << "char:" << memoryArr[4] << endl;
}

string lowerString(string str){
    for(int i =0; i<str.size(); i++){
        str[i] = tolower(str[i]);
    }
    return str;
}

int main(){
    int memoryArr[] = {0,0,0,0,0};

    while(true){
        string str = "";
        cin >> str;
        if(lowerString(str) == "quit"){
            printQuit(memoryArr);
            break;
        }
        int returnResult = printRange(str);
        memoryArr[returnResult]++;
    }
}
