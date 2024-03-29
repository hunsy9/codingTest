#include <iostream>

using namespace std;

typedef struct node
{
    int data;
    struct node *next;
} Node;
typedef struct list
{
    Node *head;
    Node *tail;
    int size;
} List;

void createlist(List *list)
{
    list->head = new Node;
    list->tail = new Node;
    list->head->next = list->tail;
    list->tail->next = list->tail;
    list->size = 0;
}
void addFirst(List *list, int data)
{
    Node *newNode = new Node;
    newNode->data = data;
    newNode->next = list->head->next;
    list->head->next = newNode;
    list->size++;
}
void addLast(List *list, int data)
{
    Node *last = list->head;

    while (last->next != list->tail)
        last = last->next;

    Node *newNode = new Node;
    newNode->data = data;
    newNode->next = list->tail;
    last->next = newNode;
    list->size++;
}

Node *searchNode(List *list, int data)
{
    Node *node = list->head->next;
    while (node != list->tail)
    {
        if (node->data == data)
            return node;
        node = node->next;
    }
    cout << "데이터를 찾지 못했습니다." << endl;

    return NULL;
}

void removeNode(List *list, int data)
{
    Node *node = list->head;
    while (node->next != list->tail)
    {
        if (node->next->data == data)
        {
            Node *delNode = node->next;
            node->next = delNode->next;
            delete (delNode);
            list->size--;
            return;
        }
        node = node->next;
    }
    cout << "데이터를 찾지 못했습니다." << endl;
}

void printList(List *list)
{
    Node *node = list->head->next;
    int i = 1;
    while (node != list->tail)
    {
        printf("%d 번째 노드 데이터 :%d\n", i++, node->data);
        node = node->next;
    }
}
void distroyList(List *list)
{
    Node *node = list->head;
    while (node != list->tail)
    {
        Node *delNode = node;
        node = delNode->next;
        delete (delNode);
    }
    delete (list->head);
    delete (list->tail);
}

int main()
{

    int i;
    List list;
    createlist(&list);

    for (i = 1; i <= 5; i++)
        addLast(&list, i);
    for (i = 11; i <= 15; i++)
        addFirst(&list, i);
    removeNode(&list, 11);
    removeNode(&list, 15);
    removeNode(&list, 5);
    removeNode(&list, 4);
    removeNode(&list, 50);

    Node *node = searchNode(&list, 14);
    cout << "search : " << node->data << endl;

    node = searchNode(&list, 12);
    cout << "search : " << node->data << endl;

    node = searchNode(&list, 3);
    cout << "search : " << node->data << endl;

    printList(&list);
    return 0;
}