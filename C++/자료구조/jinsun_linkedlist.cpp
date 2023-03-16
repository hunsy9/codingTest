#include <iostream>
#define SIZE 5

using namespace std;

class Queue
{
private:
    int items[SIZE], front, rear;

public:
    Queue();
    bool isFull();
    bool isEmpty();
    void enQueue(int element);
    int deQueue();
    void display();
};

Queue::Queue()
{
    front = -1;
    rear = -1;
}

bool Queue::isFull()
{
    if (front == 0 && rear == SIZE - 1)
    {
        return true;
    }
    if (front == rear + 1)
    {
        return true;
    }
    return false;
}

bool Queue::isEmpty()
{
    if (front == -1)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void Queue::enQueue(int element)
{
    if (isFull())
    {
        cout << "Queue is Full";
    }
    else
    {
        if (front == -1)
            front = 0;
        rear = (rear + 1) % SIZE;
        items[rear] = element;
        cout << endl
             << "Inserted " << element << endl;
    }
}

int Queue::deQueue()
{
    int element;
    if (isEmpty())
    {
        cout << "Queue is Empty" << endl;
        return (-1);
    }
    else
    {
        element = items[front];
        if (front == rear)
        {
            front = -1;
            rear = -1;
        }
        else
        {
            front = (front + 1) % SIZE;
        }
        return element;
    }
}

void Queue::display()
{
    int i;
    if (isEmpty())
    {
        cout << "Queue is Empty" << endl;
    }
    else
    {
        cout << "Front -> " << front << endl;
        cout << "Items -> ";
        for (i = front; i != rear; i = (i + 1) % SIZE)
            cout << items[i];
        cout << items[i];
        cout << endl
             << "Rear -> " << rear << endl;
    }
}