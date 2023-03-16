#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    vector<int> v;
    for (int i = 0; i < 7; i++)
    {
        v.push_back(10 * i);
    }

    vector<int>::iterator iter;
    iter = v.begin();
    for (iter = v.begin(); iter != v.end(); iter++)
        cout << *iter << " ";
    cout << endl;

    cout << &iter << endl;
    cout << *iter << endl;

    cout << v.back() << endl;
    return 0;
}