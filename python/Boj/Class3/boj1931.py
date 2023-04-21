n = int(input())
conf_time=[list(map(int,input().split())) for i in range(n)]
conf_time.sort(key=lambda time: -(time[1]-time[0]))
maxTime = max(conf_time,key=lambda time: time[1])[1]

def judge_range(time):
    return 0

table=[0]*maxTime

print(table)
for i in range(n):
    print(conf_time[i][0] , conf_time[i][1])
    print(table)
    for j in range(conf_time[i][0],conf_time[i][1]+1):
        table[j] += 1
print(conf_time)


