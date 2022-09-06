i=int(input());
m=[];

for a in range(i):
    k, l = map(int,input().split())
    m.append(k+l)

for t in range(i):
    print("Case #{}: ".format(str(t+1))+str(m[t]))