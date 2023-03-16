#수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

#Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

#X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

import sys
def isThereSameMaxValue(xyList,usedIndexList): #최댓값을 찾고 그 최댓값이랑 중복되는 인덱스가 있으면 모조리 반환하자
    copyXYList = xyList[:]
    for i in usedIndexList:
        copyXYList.remove(xyList[i])
    xyListMax = max(copyXYList)
    sameValueIndexList = list(filter(lambda x:xyList[x]==xyListMax , range(len(xyList))))
    return sameValueIndexList
def xyZip(xyList,usedIndexList): #가장 큰 값을 먼저 찾아서 좌표 압축해주는 함수
    maxValueIndexList = isThereSameMaxValue(xyList,usedIndexList) #[0]
    maxValueIndex = maxValueIndexList[0]
    mySet = set()
    count = 0
    for i in xyList: #xyList를 순회하면서
            if xyList[maxValueIndex] > i and i not in mySet: #만약 isThere함수로 가져온 maxValueIndex를 대입한 xyList값이 순회중인 xyList 값보다 크다면
                mySet.add(i)
                count+=1 #count를 증가시키자
    for index in maxValueIndexList: #압축된 좌표값은 count이다. 이제 모든 중복되는 인덱스를 한번에 바꿔주자
        xyList[index] = count
    maxValueIndexList += usedIndexList
    return xyList,maxValueIndexList

def main():
    N = int(sys.stdin.readline())
    xyList = list(map(int, sys.stdin.readline().split()))
    usedIndexList = []
    for i in range(2):
        xyList,usedIndexList = map(list,xyZip(xyList,usedIndexList))
        print(xyList)
main()
