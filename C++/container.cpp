#include "container.h"
#include <vector>

using namespace std;

int main( ) {
    int N;

    box_ready();
    N = box_size();

    vector<int> indexList(N);

    for(int i=0; i<N; i++) {
        indexList[i] = i+1;
    }

    int biggestBoxIndex = 1;
    int secondBiggestBoxIndex = 2;

    if (box_comp(1,2) == -1) {
        biggestBoxIndex = 2;
        secondBiggestBoxIndex = 1;
    }

    for(int i = 2; i < N; i++)
    {
        int comparedResult = box_comp(secondBiggestBoxIndex, indexList[i]);
        if (comparedResult == -1){
            secondBiggestBoxIndex = indexList[i];
            if(box_comp(biggestBoxIndex,secondBiggestBoxIndex) == -1){
                swap(biggestBoxIndex,secondBiggestBoxIndex);
            }
        }
    }
    box_report(secondBiggestBoxIndex);
}
