#include <string>
#include <iostream>

using namespace std;

class Rectangle {
private:
    int width, height;
public:
    //필요한 멤버함수 정의
    Rectangle( const int _width ,const int _height){
        this->width = _width;
        this->height = _height;
    }
    int getHeight(){
        return this->height;
    }
    int getWidth(){
        return this->width;
    }
    Rectangle() {

    }
};

class RectangleList{
private:
    string name;
    Rectangle* pRectangles;
    int maxSize;
    int currentIndex = 0;
public:
    RectangleList(const string& _name, const int maxSize) : name(_name){
        this->maxSize = maxSize;
        pRectangles = new Rectangle[maxSize];
    }
    ~RectangleList(){delete [] pRectangles;}
    //필요한 멤버함수정의
    void print(){
        cout << "List: " << this->name << ", Count: " << currentIndex;
        for(int i=0; i < currentIndex; i++){
            cout << " (" << (pRectangles+i)->getWidth()<< "," << (pRectangles+i)->getHeight() << ")";
        }
        cout << endl;
    }

    void swap(Rectangle& a , Rectangle& b){
        Rectangle temp;
        temp = a;
        a=b;
        b=temp;
    }

    void sort(){
        for(int i=0; i<currentIndex; i++){
            for(int j=0; j<currentIndex; j++){
                if(((this->pRectangles)+j)->getHeight() * ((this->pRectangles)+j)->getWidth() < ((this->pRectangles)+j+1)->getHeight() * ((this->pRectangles)+j+1)->getWidth())
                    swap(*((this->pRectangles)+j),*((this->pRectangles)+j+1));
            }
        }
    }

    bool add(const int a, const int b){
        Rectangle* rec = new Rectangle(a,b);
        this->pRectangles[currentIndex] = *rec;
        this->currentIndex ++;
        return true;
    }

    bool add(const RectangleList recList){
        for(int i = 0; i< recList.currentIndex; i++){
            if (this->currentIndex+1 > maxSize){
                return false;
            }
            Rectangle* rec = new Rectangle(recList.pRectangles[i].getWidth(),recList.pRectangles[i].getHeight());
            this->pRectangles[currentIndex] = *rec;
            this->currentIndex++;
        }
        return true;
    }
};

int main(){
    RectangleList list1("List1",4);

    cout << boolalpha;
    list1.print();

    cout << list1.add(10,10) << endl;
    cout << list1.add(20,20) << endl;
    cout << list1.add(15,5) << endl;

    list1.print();
    list1.sort();
    list1.print();

    RectangleList list2("List2",5);
    list2.print();

    cout << list2.add(50,10) << endl;
    cout << list2.add(10,20) << endl;
    list2.print();

    cout << list1.add(list2) << endl;
    list1.print();
    list2.print();

    list1.sort();
    list1.print();

    const RectangleList& list3 = list2;
//    list3.print();
}
