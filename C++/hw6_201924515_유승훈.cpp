#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Student {
private:
    string name;
    float gpa;
public:
    Student(string _name, float _gpa = 0) {
        name = _name;
        gpa = _gpa;
    }

    void print() const {
        cout << "Name: " << name << "GPA: " << gpa << endl;
    }

    string getName() const{
        return name;
    }

    float getGPA() const{
        return gpa;
    }

    void setName(const string& _name) {
        name = _name;
    }

    void setGPA(const float _gpa) {
        gpa = _gpa;
    }
};

class School {
private:
    string schoolName;
    vector<Student> students;
public:
    School(const string& sn) {
        schoolName = sn;
    }

    void addStudent(const string& _name, const float _gpa = 0.0F) {
        Student newStudent = Student(_name, _gpa);
        students.push_back(newStudent);
    }

    void print() {
        cout << "SchoolName: " << schoolName << ", Count: " << students.size() << endl;
        vector<Student>::const_iterator iter;
        for (iter = students.cbegin(); iter != students.cend(); iter++) {
            iter->print();
        }
        cout << endl;
    }

    void iteratorSwap(vector<Student>::iterator it1, vector<Student>::iterator it2) {
        Student temp = move(*it1);
        *it1 = move(*it2);
        *it2 = move(temp);
    }

    void sort() {
        for (int i = 0; i < students.size() - 1; i++) {
            for (int j = 0; j < students.size() - i - 1; j++) {
                if (students[j].getGPA() < students[j + 1].getGPA()) {
                    iteratorSwap(students.begin() + j, students.begin() + j + 1);
                }
            }
        }
    }

    Student& findStudentWithName(const string& _name) {
        vector<Student>::const_iterator iter;
        for (iter = students.cbegin(); iter != students.cend(); iter++) {
            if (iter->getName() == _name) {
                return const_cast<Student &>(*iter);
            }
        }
    }

};

int main() {
    School pnu("PNU");

    pnu.addStudent("Kim", 2.7F);
    pnu.addStudent("Hong", 3.5F);
    pnu.addStudent("Lee");
    pnu.addStudent("Joo", 1.5F);

    pnu.print();

    pnu.sort(); // descending
    pnu.print();

    School knu("KNU");
    knu.addStudent("Seo", 2.5F);
    knu.addStudent("Lee", 3.8F);
    knu.print();


    Student &lee = pnu.findStudentWithName("Lee");
    lee.setGPA(3.3F);
    lee.setName("Yoon");

    pnu.print();

    knu.addStudent("Hong", 4.3F);
    Student &hong = knu.findStudentWithName("Hong");
    hong.setGPA(3.3F);
    hong.setName("Joon");
    knu.print();
}