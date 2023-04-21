import sys
N = int(sys.stdin.readline())
sOwn = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

countDict = {}

for i in sOwn:
    getValue = countDict.get(i)
    if not getValue:
        countDict.update({i : 1})
    else:
        countDict[i] = getValue + 1

for j in target:
    value = countDict.get(j)
    if value:
        print(countDict.get(j), end=' ')
    else:
        print(0, end=' ')

