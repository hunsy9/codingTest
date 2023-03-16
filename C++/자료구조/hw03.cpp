#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class node
{
public:
    string data;
    node *left, *right;
};

bool getAncestors(node *root, node *node, vector<string> &vec)
{
    // 기본 케이스
    if (root == nullptr)
    {
        return false;
    }

    // 주어진 노드가 발견되면 true를 반환
    if (root == node)
    {
        return true;
    }

    // 왼쪽 하위 트리에서 노드 검색
    bool left = getAncestors(root->left, node, vec);

    // 오른쪽 하위 트리에서 노드 검색
    bool right = false;
    if (!left)
    {
        right = getAncestors(root->right, node, vec);
    }

    // 주어진 노드가 왼쪽 또는 오른쪽 하위 트리에서 발견되면
    // 현재 노드는 주어진 노드의 조상
    if (left || right)
    {
        vec.push_back(root->data);
    }

    // 노드가 발견되면 true를 반환
    return left || right;
}

node *lca(node *root, string n1, string n2)
{
    if (root == NULL)
        return NULL;

    if (root->data > n1 && root->data > n2)
        return lca(root->left, n1, n2);

    if (root->data < n1 && root->data < n2)
        return lca(root->right, n1, n2);

    return root;
}

node *newNode(string data)
{
    node *Node = new node();
    Node->data = data;
    Node->left = Node->right = NULL;
    return (Node);
}

void *insertNode(node *root, string data)
{
    node *newNode = new node(); // newNode 생성
    newNode->data = data;
    newNode->left = newNode->right = NULL;

    while (root)
    {
        if (data == root->data)
        { // 중복값
            cout << "error 중복값" << endl;
            return root;
        }
        else if (data < root->data)
        { // 왼쪽 서브트리
            if (root->left == NULL)
            { // 비어있다면 추가
                root->left = newNode;
                return root;
            }
            else
            { // 비어있지 않다면 다시 탐색 진행
                root = root->left;
            }
        }
        else
        { // key > ptr->key 오른쪽 서브트리
            if (root->right == NULL)
            { // 비어있다면 추가
                root->right = newNode;
                return root;
            }
            else
            { // 비어있지 않다면 다시 탐색 진행
                root = root->right;
            }
        }
    }
}

int main()
{
    string storedData[2] = {};
    int num;
    getline(cin, storedData[0]);
    getline(cin, storedData[1]);
    cin >> num;
    string rootString;
    getline(cin, rootString);
    node *root = newNode(rootString);
    string nodes[num];
    for (int i = 0; i < num; i++)
    {
        getline(cin, nodes[i]);
        insertNode(root, nodes[i]);
    }
    node *t = lca(root, storedData[0], storedData[1]);
    vector<string> vec;
    getAncestors(root, t, vec);
    reverse(vec.begin(), vec.end());
    for (int i = 1; i < vec.size(); i++)
    {
        cout << vec[i] << endl;
    }
    cout << t->data << endl;

    return 0;
}
