#include <iostream>
#include <vector>

using namespace std;

template<class T>
void print(const vector<T> vec){
    for(int i=1; i < vec.size(); i++){
        cout << vec[i] << " ";
    }
    cout << endl;
}

void getGrades(const vector<int> scores, vector<char>& grades){
    vector<int>::const_iterator it;
    grades.clear();
    for(it = scores.begin(); it != scores.end(); it++){
        if(*it >= 90){
            grades.push_back('A');
        }
        else if(*it >= 80){
            grades.push_back('B');
        }
        else if(*it >= 70){
            grades.push_back('C');
        }
        else if(*it >= 60){
            grades.push_back('D');
        }
        else{
            grades.push_back('F');
        }
    }
}

void addScore(vector<int>& scores ,const int i){
    vector<int>::iterator it;
    for(it = scores.begin(); it != scores.end(); it++){
        *it += i;
    }
}

int main(){
    const int SIZE = 5;
    vector<int> scores;

    const int initialValue = 100;
    for(int i=0; i<=SIZE; i++){
        scores.push_back(initialValue-i*8);
    }
    print(scores);

    vector<char> grades;
    getGrades(scores,grades);
    print(grades);

    addScore(scores,5);
    print(scores);

    getGrades(scores,grades);
    print(grades);
}
