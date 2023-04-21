import math

result = 100000000000
answer = 100000000001
len = 100000000000

s1 = [0,0,0]
s2 = [0,0,0]
def getDistance(pos1, pos2):
    return math.sqrt(sum([(pos1i-pos2i)**2 for pos1i, pos2i in zip(pos1,pos2)]))
def solve():
    global result
    global answer

    s1[0] = aPos[0]
    s1[1] = aPos[1]
    s1[2] = aPos[2]

    lengthOfAB = round(getDistance(aPos,bPos))
    lengthOfCD = round(getDistance(cPos,dPos))

    for i in range(lengthOfAB):
        if result < answer:
            answer = result
        else:
            print(math.ceil(answer))
            break
        s2[0] = cPos[0]
        s2[1] = cPos[1]
        s2[2] = cPos[2]
        for j in range(lengthOfCD):
            len = getDistance(s1,s2)
            if(len <= result):
                result=len
            for k in range(3):
                s2[k] += ((dPos[k]-cPos[k])/lengthOfCD)
        for l in range(3):
            s1[l] += ((bPos[l] - aPos[l]) / lengthOfAB)

aPos = list(map(float, input().split()))
bPos = list(map(float, input().split()))
cPos = list(map(float, input().split()))
dPos = list(map(float, input().split()))

solve()

