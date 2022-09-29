#include <string>
#include <iostream>

using namespace std;

struct Person{
    std::string name;
    std::string id;
    string age;
};

class president {
    private:
        string name_="";
        string age_ = "";
        string nation_="";
    public:
    void inputPresident();
    void printPresident();
   
};

void president :: inputPresident(){

        cout << "대통령의 이름을 입력하세요" << endl;
        cin >> name_;
        
        cout << "대통령의 나이를 입력하세요" << endl;
        cin >> age_;

        cout << "대통령의 국적을 입력하세요" << endl;
        cin >> nation_;

}

void president::printPresident(){
    cout << "이름: " << name_ << endl << "나이: " << age_ <<endl<< "국적: " << nation_ <<endl;
}


void goodfunction(Person p){
cout << "이름을 입력하세요: ";
cin >> p.name;
p.id = "201924515";
p.age = 23;

cout << p.name <<endl;
}

int main(){
Person seunghun;
president no = president();

goodfunction(seunghun);

no.inputPresident();
no.printPresident();


}







