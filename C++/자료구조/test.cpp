#include <iostream>
#include <queue>
using namespace std;

class Person
{
public:
    int a;
    int b;
    int c;

    bool operator>(const Person &a)
    {
        if (this->b > a.b)
            return true;
        else
            return false;
    }
};

int main()
{
    priority_queue<Person> myP;

    Person p1 = Person();
    p1.a = 1;
    p1.b = 10;
    p1.c = 4;

    Person p2 = Person();
    p2.a = 1;
    p2.b = 20;
    p2.c = 4;

    Person p3 = Person();
    p3.a = 1;
    p3.c = 15;
    p3.c = 4;

    myP.push(p1);
    myP.push(p2);
    myP.push(p3);

    while (!myP.empty())
    {
        Person temp = myP.top();
        myP.pop();

        cout << temp.b << " ";
    }
}