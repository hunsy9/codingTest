#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Item {
    string name;
    double price;
    int quantity;
};

void print_iter(vector<Item>::iterator it){
    cout << "Item found: " << it->name << " " << it->price << " " << it->quantity << endl;
}

void print_count(const int count){
    cout << "Number of expensive items: " << count << endl;
}

int main() {
    vector<Item> inventory = {
            {"Apple", 0.99, 10},
            {"Banana", 0.59, 20},
            {"Cherry", 1.49, 5},
            {"Dates", 2.99, 2},
            {"Elderberry", 3.99, 0},
            {"Fig", 2.49, 15},
            {"Grape", 0.79, 25},
            {"Honeydew", 1.29, 8},
            {"Indian Gooseberry", 2.99, 0},
            {"Jackfruit", 4.99, 1}
    };
    sort(inventory.begin(),inventory.end(), [](Item item1, Item item2){ return item1.price < item2.price; }));

    for_each(inventory.begin(),inventory.end(), [](Item item){ cout << item.name << " " << item.price << " " << item.quantity << endl; });

    print_iter(find_if(inventory.begin(),inventory.end(), [](Item item){ return item.name == "Grape";});)

    print_count(count_if(inventory.begin(),inventory.end(),[](Item item){ return item.price > 2.48; });)

    inventory.erase(remove_if(inventory.begin(),inventory.end(), [](Item item){ return item.quantity == 0; }), inventory.end());

    for_each(inventory.begin(),inventory.end(), [](Item item){ cout << item.name << " " << item.price << " " << item.quantity << endl; });

    return 0;
}
