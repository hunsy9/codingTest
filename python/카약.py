a1, a2 , a3 = map(int,input().split())
sonsang = list(map(int, input().split()))
good = list(map(int, input().split()))
team = list()
for i in range(a1):
    team.append(1)
print(team)
for i in sonsang:
    team[i-1]+=(-1)
print(team)
for i in good:
    team[i-1]+=1
print(team)
count = team.count(0)
count1 = 0
for i in range(len(team)):
    if abs(team[i]-team[i+1])==2:
        count1+=1

print(count1)




