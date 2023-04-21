#include "iostream"
#include "string"

using namespace std;

string lowerString(string str){
    for(int i =0; i<str.size(); i++){
        str[i] = tolower(str[i]);
    }
    return str;
}

void add(int* const scores, int* addCount, int maxSize){
    int addingScore = 0;
    if(*addCount >= maxSize){
        cout << "Too many scores" << endl;
        return;
    }
    cout << "Enter score: ";
    cin >> addingScore;
    if(addingScore>100 || addingScore < 0){
        cout << "Score should be between 0 and 100" << endl;
        return;
    }
    scores[*addCount] = addingScore;
    cout << addingScore << " added" << endl;
    *addCount = *addCount + 1;
}

void sum(int* const scores, int addCount){
    int sum = 0;
    for(int i=0; i < addCount; i++){
        sum += scores[i];
    }
    cout << "Sum: " << sum << endl;
}

void average(int* const scores, int maxSize, int addCount){
    int sum = 0;
    for(int i=0; i < maxSize; i++){
        sum += scores[i];
    }
    double average = double(sum) / addCount;
    cout << "Average: " << average << endl;
}

void list(int* const scores , int addCount){
    for(int i=0; i < addCount; i++){
        if( i == addCount-1){
            cout << scores[i] << endl;
            return;
        }
        cout << scores[i] << ", ";
    }
}

int main() {
    cout << "Enter the score count: " ;
    int maxSize ;
    cin >> maxSize ;

    int* const scores = new int[maxSize];

    int addCount = 0;

    while(true){
        string command="";
        cout << "Enter command: (add, sum, average, list, quit) ";
        cin >> command;
        command = lowerString(command);

        if(command == "quit"){
            cout << "Bye" << endl;
            break;
        }

        if(command == "add"){
            add(scores, &addCount, maxSize);
        }

        if(command == "sum"){
            sum(scores,addCount);
        }

        if(command == "average"){
            average(scores,maxSize,addCount);
        }

        if(command == "list"){
            list(scores,addCount);
        }
    }

    delete [] scores ;
}
