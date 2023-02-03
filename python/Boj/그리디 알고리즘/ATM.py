a = int(input())
timeList=sorted(list(map(int,input().split())))

person=list(range(a))
totalSum=0
for i in range(a):
    person[i]=0
    personSum = 0
    for j in list(range(i+1)):
        personSum+=timeList[j]
    totalSum += personSum
print(totalSum)
