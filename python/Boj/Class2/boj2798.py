N,M=map(int, input().split())
cards= list(map(int, input().split()))
cards.sort(reverse=True)
temp=[]
print(cards)
sum = 0
for i in range(N):
    sum += cards[i]
    for j in range(i+1,N):
        sum += cards[j]
        for k in range(j+1,N):
            sum += cards[k]
            if sum <= M:
                print(sum)
                temp.append(sum)
            sum = 0
print(max(temp))







