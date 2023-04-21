#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

enum CommandKind { ADD, SORT, PRINT, CLEAR, EXIT, INVALID} ;

struct Rectangle {
    int width ;
    int height ;
} ;

void iteratorSwap(vector<Rectangle>::iterator it1, vector<Rectangle>::iterator it2)
{
    Rectangle temp = move(*it1);
    *it1 = move(*it2);
    *it2 = move(temp);
}

void print(vector<Rectangle> rectangles){
    vector<Rectangle>::iterator it;
    cout << "Rectangle Count: "<< rectangles.size() << endl;
    for(it = rectangles.begin(); it!=rectangles.end(); it++){
        cout << it->height <<" "<< it->width <<" "<< it->height*it->width << endl;
    }
}

void sort(vector<Rectangle>& rectangles){
    for(int i = 0; i < rectangles.size()-1; i++) {
        for(int j = 0; j < rectangles.size()-i-1; j++) {
            if(rectangles[j].height > rectangles[j+1].height) {
                iteratorSwap(rectangles.begin()+j, rectangles.begin()+j+1);
            }
        }
    }
}

CommandKind getCommandKind(string commandString){
    if(commandString == "ADD"){
        return ADD;
    }
    if(commandString == "PRINT"){
        return PRINT;
    }
    if(commandString == "SORT"){
        return SORT;
    }
    if(commandString == "CLEAR"){
        return CLEAR;
    }
    if(commandString == "EXIT"){
        return EXIT;
    }
    if(commandString == "INVALID"){
        return INVALID;
    }
}

Rectangle getRectangle(){
    int height = 0;
    int width = 0;
    cin >> height >> width;
    Rectangle newRectangle;
    newRectangle.height = height;
    newRectangle.width = width;
    return newRectangle;
}

int main() {
    vector<Rectangle> rectangles ;
    while ( true ) {
        string commandString;
        cin >> commandString;
        const CommandKind command = getCommandKind(commandString) ;
        switch ( command ) {
            case ADD : {
                const Rectangle& newRectangle = getRectangle() ;
                rectangles.push_back(newRectangle) ;
                break ;
            }
            case PRINT:
                print(rectangles) ;
                break ;
            case SORT: {
                sort(rectangles) ; // define and call swap in sort()
                print(rectangles) ;
                break ;
            }
            case CLEAR:  rectangles.clear() ; break ;
            case EXIT: break ;
            default:  assert (false) ; break ;
        }
        if ( command == EXIT ) break ;
    }
}