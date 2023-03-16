#include <iostream>

using namespace std;

namespace BestComIpl
{
    void SimpleFunc(void);
}
namespace ProgComIpl
{
    void SimpleFunc(void);
}

int main(void){
    BestComIpl::SimpleFunc();
    ProgComIpl::SimpleFunc();
    return 0;
}

void BestComIpl::SimpleFunc(void){
    {
        cout << "BestCom이 정의한 함수"<<endl;
    }
}
void ProgComIpl::SimpleFunc(void){
    {
        cout << "ProgComIpl이 정의한 함수"<<endl;
    }
}