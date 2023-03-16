#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Node
{
    friend class HashTable;

private:
    string key;
    int data;
    Node *next;

public:
    Node(string nodeKey, int nodeData)
    {
        key = nodeKey;
        data = nodeData;
        next = NULL;
    }
    string getNodeKey(Node *node)
    {
        return node->key;
    }
};

class HashTable
{
private:
    vector<Node *> table;
    int a_value;
    int n;

public:
    HashTable(int a, int n = 512)
    {
        table.resize(n);
        a_value = a;
    }
    int getN()
    {
        return n;
    }
    int moreThanfive(HashTable *h)
    {
        int sum = 0;
        for (int i = 0; i < n; i++)
        {
            int temp = 0;
            if (h->table[i] != NULL)
            {
                Node *curNode = h->table[i];
                while (curNode != NULL)
                {
                    curNode = curNode->next;
                    temp++;
                }
            }
            if (temp > 5)
            {
                sum++;
            }
        }
        return sum;
    }

    int longestBucketIndex(HashTable *h)
    {
        int sum = 0;
        int index = 0;
        for (int i = 0; i < n; i++)
        {
            int temp = 0;
            if (h->table[i] != NULL)
            {
                Node *curNode = h->table[i];
                while (curNode != NULL)
                {
                    curNode = curNode->next;
                    temp++;
                }
            }
            if (sum <= temp)
            {
                index = i;
                sum = temp;
            }
        }
        return index;
    }

    int getNumEntries(HashTable *h)
    {
        int sum = 0;
        for (int i = 0; i < n; i++)
        {
            if (h->table[i] != NULL)
            {
                Node *curNode = h->table[i];
                while (curNode != NULL)
                {
                    curNode = curNode->next;
                    sum++;
                }
            }
        }
        return sum;
    }

    HashTable *reHashing(HashTable *hashTable, float min, float max, float curLoadFactor, int a_value)
    {
        int currentSize = hashTable->getN();

        if (curLoadFactor > max)
        {
            HashTable *newTable = new HashTable(a_value, currentSize * 2);
            cout << "Rehashing: " << currentSize << " -> " << currentSize * 2 << endl;
            for (int i = 0; i < currentSize; i++)
            {
                if (hashTable->table[i] != nullptr)
                {
                    Node *node = hashTable->table[i];
                    while (node->next)
                    {
                        int index = hashTable->hashFunc(node->getNodeKey(node));
                        newTable->insertNode(node, index);
                        node = node->next;
                    }
                }
            }
            return newTable;
        }
        if (curLoadFactor < min)
        {
            HashTable *newTable = new HashTable(a_value, currentSize / 2);
            cout << "Rehashing: " << currentSize << " -> " << currentSize / 2 << endl;
            for (int i = 0; i < currentSize; i++)
            {
                if (hashTable->table[i] != nullptr)
                {
                    Node *node = hashTable->table[i];
                    while (node->next)
                    {
                        int index = hashTable->hashFunc(node->getNodeKey(node));
                        newTable->insertNode(node, index);
                        node = node->next;
                    }
                }
            }
            return newTable;
        }
    }

    long fx(long num)
    {
        return (num % 2147483647);
    }

    long hashFunc(string nodeKey)
    {
        long hash = 0;
        for (int i = 0; i < nodeKey.length(); i++)
        {
            if (i == nodeKey.length() - 1)
            {
                hash = fx(hash + int(nodeKey[i]));
            }
            else
            {
                hash = a_value * fx(hash + long(nodeKey[i]));
            }
        }
        return hash % n;
    }

    void insertNode(Node *node, int index)
    {
        cout << index << endl;
        Node *curNode;
        curNode = table[index];
        // if (curNode == nullptr)
        // {
        //     curNode = node;
        // }
        // else
        // {
        //     while (curNode->next != NULL)
        //     {
        //         curNode = curNode->next;
        //     }
        //     curNode->next = node;
        // }
    }

    void removeNode(string id, HashTable *h)
    {
        int hashKey = h->hashFunc(id);
        if (h->table[hashKey] == nullptr)
        {
            return;
        }
        Node *deleteNode = nullptr;
        if (h->table[hashKey]->key == id)
        {
            deleteNode = h->table[hashKey];
            h->table[hashKey] = h->table[hashKey]->next;
        }
        else
        {
            Node *curNode = h->table[hashKey];
            Node *nextNode = curNode->next;
            while (nextNode != nullptr)
            {
                if (nextNode->key == id)
                {
                    curNode->next = nextNode->next;
                    deleteNode = nextNode;
                    break;
                }
                curNode = nextNode;
                nextNode = curNode->next;
            }
        }
        delete (deleteNode);
    }

    void printResult(HashTable *h)
    {
        cout << "Number of entries: " << getNumEntries(h) << endl;
        cout << "Size of the bucket array: " << n << endl;
        cout << moreThanfive(h) << " buckets contain more than 5 elements" << endl;
        int lbi = longestBucketIndex(h);
        cout << "The longest bucket: " << lbi << endl;
        Node *curNode = h->table[lbi];
        while (curNode != NULL)
        {
            cout << "(" << curNode->key << "," << curNode->data << ")" << endl;
            curNode = curNode->next;
        }
    }
};

int main()
{
    int a;
    float min_load_factor;
    float max_load_factor;
    int numOfLines;

    cin >> a >> min_load_factor >> max_load_factor;
    cin >> numOfLines;
    HashTable *hashTable = new HashTable(a);

    for (int i = 0; i < numOfLines; i++)
    {
        float loadFactor = hashTable->getNumEntries(hashTable) / hashTable->getN();
        string mode;
        string key;
        int data;

        cin >> mode >> key >> data;
        int index = hashTable->hashFunc(key);
        if ((hashTable->getN() > 512 && loadFactor < min_load_factor) || loadFactor > max_load_factor)
        {
            hashTable = hashTable->reHashing(hashTable, min_load_factor, max_load_factor, loadFactor, a);
        }
        if (mode == "i")
        {
            Node *newNode = new Node(key, data);
            hashTable->insertNode(newNode, index);
        }
        // else if (mode == "r")
        // {
        //     // hashTable->removeNode(key, hashTable);
        // }
    }
    hashTable->printResult(hashTable);
    return 0;
}
