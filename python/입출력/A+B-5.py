k=[]
while True:
    m, n = map(int,input().split());
    if m==0 & n==0:
        break;
    k.append(m+n)
for i in range(len(k)):
    print(k[i])


