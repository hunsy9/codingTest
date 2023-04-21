//#include <iostream>
//#include <math.h>
//
//using namespace std;
//
//double x, y, z;
//double result = 100000000000, answer=100000000001, len=100000000000;
//double s1[3], s2[3];
//double vec[4][3];
//
//double getDistance(double pos1[3], double pos2[3]) {
//    len = (pos1[0] - pos2[0]) * (pos1[0] - pos2[0]);
//    len += (pos1[1] - pos2[1]) * (pos1[1] - pos2[1]);
//    len += (pos1[2] - pos2[2]) * (pos1[2] - pos2[2]);
//    return len;
//}
//
//void input() {
//    for(int i=0; i<4; i++) {
//        cin >> x >> y >> z;
//        vec[i][0] = x;
//        vec[i][1] = y;
//        vec[i][2] = z;
//    }
//}
//
//void solve() {
//    for(int k=0; k<3; k++) {
//        s1[k] = vec[0][k];
//    }
//    double lengthOfAB = sqrt(getDistance(vec[0], vec[1]));
//    double lengthOfCD = sqrt(getDistance(vec[2], vec[3]));
//
//    for(int i=0; i < lengthOfAB; i++) {
//        if (result < answer) answer = result;
//        else break;
//        s2[0] = vec[2][0];
//        s2[1] = vec[2][1];
//        s2[2] = vec[2][2];
//        for(int j=0; j < lengthOfCD; j++) {
//            len = getDistance(s1, s2);
//            if(len <= result) result = len;
//            s2[0] += ((vec[3][0] - vec[2][0]) / lengthOfCD);
//            s2[1] += ((vec[3][1] - vec[2][1]) / lengthOfCD);
//            s2[2] += ((vec[3][2] - vec[2][2]) / lengthOfCD);
//        }
//        s1[0] += ((vec[1][0] - vec[0][0]) / lengthOfAB);
//        s1[1] += ((vec[1][1] - vec[0][1]) / lengthOfAB);
//        s1[2] += ((vec[1][2] - vec[0][2]) / lengthOfAB);
//    }
//    cout << round(sqrt(answer)) << endl;
//}
//
//int main() {
//    input();
//    solve();
//    return 0;
//}


