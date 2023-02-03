N=int(input())
dung=[list(map(int,input().split())) for i in range(N)]
dung.sort(key=lambda x:(-x[0],-x[1]))
print(dung)