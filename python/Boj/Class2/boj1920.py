import sys
N=int(sys.stdin.readline())
targetSet = set(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
varList = list(map(int,sys.stdin.readline().split()))


for i in varList:
    if i in targetSet:
        print(1)
    else:
        print(0)
