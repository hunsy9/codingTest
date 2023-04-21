#include <iostream>
#include <vector>

using namespace std;

const int SUBJECT_NO = 3 ;

struct StudentInfo {
    string name ;
    int scores[SUBJECT_NO] ;
    int sum ;
    float average ;
};

int getSum(int scores[]){
    return scores[0] + scores[1] + scores[2];
}

void printStudentInfo(int index ,StudentInfo studentInfo){
    cout << index <<"    "<< studentInfo.name <<"  "<< studentInfo.scores[0] <<"  "<< studentInfo.scores[1] <<"  "<< studentInfo.scores[2] <<"  "<< studentInfo.sum <<"  "<< studentInfo.average << endl;
}

void printVector(vector<StudentInfo> studentInfoVec){
    vector<StudentInfo>::iterator iter;
    int scoreSum[SUBJECT_NO] = {0,};
    int sumOfSum = 0;
    int index = 1;
    for(iter = studentInfoVec.begin(); iter != studentInfoVec.end(); iter++){
        scoreSum[0] += iter->scores[0];
        scoreSum[1] += iter->scores[1];
        scoreSum[2] += iter->scores[2];
        sumOfSum += iter->sum;
        printStudentInfo(index++,*iter);
    }
    cout << "Total" <<"    "<< scoreSum[0] <<"    "<< scoreSum[1] <<"   "<< scoreSum[2] <<"   "<< sumOfSum <<"    "<< endl;
}

int main(){
    vector<StudentInfo> studentInfoVec;
    int studentNumber = 0;
    cin >> studentNumber;
    for(int i=0; i < studentNumber; i++){
        struct StudentInfo studentInfo;
        cin >> studentInfo.name >> studentInfo.scores[0] >> studentInfo.scores[1] >> studentInfo.scores[2];
        studentInfo.sum = getSum(studentInfo.scores);
        studentInfo.average = static_cast<float>(studentInfo.sum) / 3.0;
        studentInfoVec.push_back(studentInfo);
    }
    printVector(studentInfoVec);
}
