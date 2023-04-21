N,M=map(int, input().split())
cards= sorted(list(map(int, input().split())))

sumSet = set()
sum=0
for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= M:
                sumSet.add(sum)
            sum = 0
print(max(sumSet))











