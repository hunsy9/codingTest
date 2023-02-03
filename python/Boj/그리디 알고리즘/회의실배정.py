a= int(input())
bigList=[]
for i in range(a):
    babyList=list(map(int,input().split()))
    bigList.append(babyList)
print(str(bigList))
for i in range(len(bigList)):
    for j in range(len(bigList)-1):
        if list(range(bigList[i][0],bigList[i][1]))[0] <= list(range(bigList[j+1][0],bigList[j+1][0]))[0] and list(range(bigList[i][0],bigList[i][1]))[-1] <= list(range(bigList[j+1][0],bigList[j+1][1]))[-1]:
            bigList.remove(bigList[j+1])
print(bigList)