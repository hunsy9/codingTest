import sys
import time

N = int(sys.stdin.readline())

start1 = time.time()
i = 1
layerRangeMax = 1
layerRangeMin = 2
while True:  # layer의 범위를 지정해서 그 범위안에 있으면 결과를 도출하는 방식으로 풀었다
    layerRangeMax += 6 * i
    layerRangeMin += 6 * (i - 1)
    # print("layer: {} to {}".format(layerRangeMin,layerRangeMax))
    if N > layerRangeMin and N < layerRangeMax:
        print(i + 1)
        break
    else:
        i += 1
end1 = time.time()
print("Algorithm1 time:{}".format(end1 - start1))

# 하지만 문제조건이 1<x<십억이라서 십억을 넣어보니 20초가 걸린다..
# while문을 안돌리는 방향으로 가보자.
# 예 58
start2 = time.time()
a=N//6
b=N%6
count =0
i=1
while True:
    if a<0:
        if b != 0:
            print(count+1)
            break
    a -= i
    count+=1
    i += 1
end2 = time.time()
print("Algorithm2 time:{}".format(end2 - start2))


start = time.time()
index = 0 #count
num = 1
while True:
    if N==1:
        print(1)
        break
    if num >= N:
        print(index)
        break
    num += 6 * index
    index += 1
end = time.time()
print("Algorithm3 time:{}".format(end - start))
