#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int N, fish;
vector <int> fishes;
vector <int> fliped;

bool isFliped() {
    for (int i=0; i<N; i++) {
        if (fliped[i] != i+1) return false;
    }
    return true;
}

void flip(int m, int n) {
    reverse(fliped.begin()+m, fliped.begin()+n+1);

    for (int i=m; i< n+1; i++) {
        fliped[i] *= -1;
    }
}


bool possible(int k) {
    for (int i=k; i <N; i++) {
        if (fliped[i] != i+1) {
            for (int j = 0; j<N; j++) {
                if (abs(fliped[j])==i+1) {
                    flip(min(j, i), max(j, i));
                    return isFliped();
                }
            }
        }
    }
    return false;
}


void result() {
    for (int i=0; i<N; i++) {
        fliped.assign( fishes.begin(), fishes.end() );

        if (possible(i)) { cout << "one" << endl; return; }
        else {
            if (possible(0)) { cout << "two" << endl; return; }
        }
    }
    cout << "over" << endl;
}


int main() {
    cin >> N;
    for (int i=0; i<5; i++) {
        fishes.clear();
        for (int j=0; j<N; j++) {
            cin >> fish;
            fishes.push_back(fish);
        }
        result();
    }
    return 0;
}

