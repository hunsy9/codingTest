#include <iostream>
#include <string>

using namespace std;

string LCQS[101][101];
string S, T;
string answer = "";

void calLongest(int m, int n) {
    for (int i=m; i<m+2; i++) {
        for (int j=n; j<n+2; j++) {
            if(i>=S.length() || j>=T.length()) continue;
            else if (m == 0 || n == 0) {
                if (LCQS[i][j] == "") LCQS[i][j] = S[m];
            }
            else {
                if (LCQS[i][j].length() < (LCQS[m-1][n-1]+S[m]).length()) {
                    LCQS[i][j] = LCQS[m-1][n-1]+S[m];
                }
                else if (LCQS[i][j].length() == (LCQS[m-1][n-1]+S[m]).length()) {
                    LCQS[i][j] = min(LCQS[i][j], LCQS[m-1][n-1]+S[m]);
                }
            }
            if(LCQS[i][j].length() > answer.length()) answer = LCQS[i][j];
            else if(LCQS[i][j].length() == answer.length()) answer = min(answer, LCQS[i][j]);
        }
    }
}

int main() {
    cin >> S >> T;

    for (int i=0; i<S.length(); i++) {
        for (int j=0; j<T.length(); j++) {
            if (S[i] == T[j]) calLongest(i, j);
        }
    }

    cout << answer << endl;

    return 0;
}