#include <iostream>

using namespace std;

struct node
{
    int data;
    node *nextNode;
};

class LinkedList
{
private:
    node *head;
    node *tail;

public:
    LinkedList()
    {
        // head 와 tail의 포인터를 초기화;
        head = NULL;
        tail = NULL;
    }
    //첫번째의 node 추가
    void addFrontNode(int n);
    //마지막의 node 추가
    void addNode(int n);

    // node 삽입
    void insertNode(node *prevNode, int n);
    // node 삭제
    void deleteNode(node *prevNode);

    //첫번째 노드 가져오기
    node *getHead()
    {
        return head;
    }
    // LinkedList 출력
    void display(node *head);
};

void LinkedList::addFrontNode(int n)
{
    node *temp = new node;
    temp->data = n;
    if (head == NULL)
    {
        head = temp;
        tail = temp;
    }
    else
    {
        temp->nextNode = head;
        head = temp;
    }
}

void LinkedList::addNode(int n)
{
    node *temp = new node;
    temp->data = n;
    temp->nextNode = NULL;
    if (tail == NULL)
    {
        head = temp;
        tail = temp;
    }
    else
    {
        tail->nextNode = temp;
        tail = temp;
    }
}

void LinkedList::insertNode(node *prevNode, int n)
{
    node *temp = new node;
    temp->data = n;
    temp->nextNode = prevNode->nextNode;
    prevNode->nextNode = temp;
}

void LinkedList::deleteNode(node *prevNode)
{
    node *temp = prevNode->nextNode;
    prevNode->nextNode = temp->nextNode;
    delete temp;
}

void LinkedList::display(node *head)
{
    if (head == NULL)
    {
        cout << "링크드 리스트가 빈 상태입니다.\n";
    }
    else
    {
        cout << head->data << endl;
        display(head->nextNode);
    }
}

int main(void)
{
    LinkedList a;
    a.addNode(1);
    a.addNode(2);
    a.addNode(3);
    a.display(a.getHead());

    a.deleteNode(a.getHead()->nextNode);
    a.display(a.getHead());

    return 0;
}