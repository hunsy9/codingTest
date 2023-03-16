#include <iostream>
#include <string>
#define null 0
using namespace std;

class Tree;

class TreeNode
{
    friend class Tree;

private:
    string data;
    TreeNode *left;
    TreeNode *right;

public:
    TreeNode(string data = "", TreeNode *left = null, TreeNode *right = null)
    {
        this->data = data;
        this->left = left;
        this->right = right;
    }
};

class Tree
{
private:
    TreeNode *root;

public:
    Tree(string data)
    {
        root = new TreeNode(data);
    }
    void setRoot(string data)
    {
        root = new TreeNode(data);
    }

    TreeNode *findNode(TreeNode *tree, string data)
    {
        char temp1[256];
        char temp2[256];
        strcpy(temp1, tree->data.c_str());
        strcpy(temp2, data.c_str());
        int compare = strcmp(temp1, temp2);
        if (tree == NULL)
        {
            return NULL;
        }
        if (compare == 0)
        {
            return tree;
        }
        else if (compare == 1)
        {
            return findNode(tree->left, data);
        }
        else if (compare == -1)
        {
            return findNode(tree->right, data);
        }
    }

    TreeNode *getRoot()
    {
        return root;
    }

    void addNode(TreeNode *prev, TreeNode *next)
    {
        char temp1[256];
        char temp2[256];
        strcpy(temp1, prev->data.c_str());
        strcpy(temp2, next->data.c_str());
        int compare = strcmp(temp1, temp2);
        if (compare == -1)
        {
            prev->right = next;
        }
        if (compare == 1)
        {
            prev->left = next;
        }
    }

    void *commonAncester(TreeNode *root, string str1, string str2)
    {
        if (root == NULL)
        {
            return NULL;
        }
        if (root->data > str1 && root->data < str2)
        {
            return commonAncester(root->left, str1, str2);
        }
        if (root->data < str1 && root->data > str2)
        {
            return commonAncester(root->right, str1, str2);
        }
    }
};

int main()
{
    Tree tree("");
    string start;

    string storedData[2] = {};
    int num;
    for (int i = 0; i < 3; i++)
    {
        cin >> storedData[i];
        if (i == 2)
        {
            cin >> num;
        }
    }
    string nodes[num];
    for (int i = 0; i < num; i++)
    {
        string str;
        if (i == 0)
        {
            getline(cin, start);
            cout << start << endl;
            tree.setRoot(start);
        }
        getline(cin, nodes[i]);
        if (i == 1)
        {
            tree.addNode(tree.getRoot(), new TreeNode(nodes[i], NULL, NULL));
        }
        else
        {
            tree.addNode(tree.findNode(tree.getRoot(), nodes[i - 1]), new TreeNode(nodes[i], NULL, NULL));
        }
    }
    TreeNode *getroot = tree.getRoot();
    cout << tree.commonAncester(getroot, storedData[0], storedData[1]);
}
