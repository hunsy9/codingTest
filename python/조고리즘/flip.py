from collections import deque
def judge(originArr, targetArr):
    test = []
    dq = deque()
    s = set()
    complexCount = 0
    for i in range(len(originArr)):
        diff = originArr[i] - targetArr[i]
        test.append(diff)
        if len(dq)!=0 and dq[-1] != diff and diff != 0:
            complexCount += 1
        if diff != 0: # 0이 아닐때
            s.add(diff)
            dq.append(diff)
        else: # 0일때
            if len(dq)!=0 and dq[-1] != 0:
                dq.append(diff)
    for j in range(len(dq)):
        if dq[0] == 0:
            dq.popleft()
        if dq[-1] == 0:
            dq.pop()
    diffNumCount = len(s) #set을 이용하여 갯수 종류 파악
    betweenZeroCount = dq.count(0) ## 숫자사이에 낀 0의 갯수를 파악
    minusCount = len([x for x in dq if x < 0])
    print("dq: ",dq)
    print("complexity: ", complexCount)
    print("originalDiffList: ",test)
    print("sum of originalDiffList: ",sum(test))
    print("diffNumCount:", diffNumCount)
    print("betweenZeroCount:", betweenZeroCount)
    print("minusCount: ", minusCount)
    if diffNumCount == 1 and betweenZeroCount == 0:
        print("one")
        return
    if diffNumCount == 2 and minusCount != 0 and complexCount > 1:
        print("over")
        return
    if (diffNumCount == 1 and diffNumCount == 1) or (diffNumCount == 2 and betweenZeroCount < 2) or (diffNumCount == 3 and betweenZeroCount == 0):
        print("two")
        return
    else:
        print("over")

N = int(input())
originArray = list(range(1,N+1))
for i in range(5):
    targetArr = list(map(int,input().split()))
    if len(list(filter(lambda x: x < 0 , targetArr))) == 0:
        print("over")
        continue
    judge(originArray,targetArr)

