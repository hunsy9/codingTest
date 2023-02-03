import sys
N,count=map(int,sys.stdin.readline().split())
trees=list(map(int, sys.stdin.readline().split()))
for i in range(max(trees)+1,1,-1):
    upperTree = []
    for j in range(N):
        if trees[j] > i:
            upperTree.append(trees[j]-i)
        else:
            upperTree.append(0)
    if count == sum(upperTree):
        print(i)
        break






