#include <iostream>

using namespace std;

class Stack1
{
private:
    int maxStackSize;
    int top;
    int stack[100] = {
        0,
    };

public:
    Stack1(int maxStackSize);
    void isFull();
    void isEmpty();
    void push(int item);
    void pop();
    void showStack();
};

Stack1::Stack1(int maxStackSize)
{
    maxStackSize = maxStackSize;
    top = -1;
}

void Stack1::isFull()
{
    if (top >= maxStackSize - 1)
    {
        cout << "스택이 꽉찼습니다." << endl;
    }
}

void Stack1::isEmpty()
{
    if (top == -1)
    {
        cout << "스택이 비었습니다." << endl;
    }
}

void Stack1::push(int item)
{
    if (top >= maxStackSize - 1)
    {
        isFull();
    }
    else
    {
        stack[++top] = item;
        cout << top << "번째에" << item << "이 push 되었습니다." << endl;
    }
}
void Stack1::pop()
{
    if (top == -1)
    {
        isEmpty();
    }
    else
    {
        cout << top << "번째에"
             << "이 pop 되었습니다." << endl;
        top--;
    }
}
void Stack1::showStack()
{
    if (top == -1)
    {
        isEmpty();
    }
    else
    {
        cout << "현재 스택에 존재하는 숫자는" << endl;
        for (int i = 0; i < maxStackSize; i++)
        {
            cout << stack[i] << " ";
        }
        cout << "\n";
    }
}

int main(void)
{
    int maxStackSize = 0;
    cout << "스택의 크기를 입력하세요:\n";
    cin >> maxStackSize;

    Stack1 s(maxStackSize);

    int choice = 0;
    int item = 0;
    cout << "\n원하는 작업을 선택하세요\n"
            "(1)pop (2)push (3)ShowStack (4)종료:\n";
    cin >> choice;
    while (choice != 4)
    {

        switch (choice)
        {
        case 1:
            s.pop();
            break;

        case 2:
            cout << "\n삽입할 수를 입력하세요:\n";
            cin >> item;
            s.push(item);
            break;

        case 3:
            s.showStack();
            break;
        }

        cout << "\n원하는 작업을 선택하세요\n"
                "(1)pop (2)push (3)ShowStack (4)종료:\n\n";

        cin >> choice;
    }

    return 0;
}