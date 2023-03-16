#include <iostream>
#include <string>
#include <stack>


using namespace std;

int main(){

    stack<string> st;

    std::string a;

    std::cin >> a;
    int j = 0;
    while(j < a.size()){
        cout << a[j] << endl;
        j++;
    }
    st.push(a);
    cout << st.top() << endl;
    int i = a.size();
    cout << "len : " << i << ", " << "string : "<< a << endl;
    cout << a[3]<< endl;

    
}
