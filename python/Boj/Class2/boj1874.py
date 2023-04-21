N=int(input())
stackSeqeunce = [int(input()) for i in range(N)]
originalSequence = list(range(1,N+1))
tempStack = []
stringStack = []
count = 0
for s in stackSeqeunce:
    if s == originalSequence[count]:
        stringStack.append("-")
        count += 1
    if s in tempStack:
        for j in reversed(tempStack):
            tempStack.pop()
            stringStack.append("-")
            if j == s:
                break
    else:
        diff = abs(s-originalSequence[count])
        for i in range(diff+1):
            if tempStack[-1] == s:
                tempStack.pop()
                stringStack.append("-")
                count+=1
            else:
                stringStack.append("+")
                tempStack.append(originalSequence[count])
                count += 1

    print(tempStack)
print(stringStack)

