import sys
N=int(sys.stdin.readline())
a=[int(sys.stdin.readline()) for i in range(N)]
a.sort()
for i in a:
    print(i)