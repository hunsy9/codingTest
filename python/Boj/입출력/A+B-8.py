i=int(input());
m=[];
x=[];

for a in range(i):
    k, l = map(int,input().split())
    m.append(k+l)
    x.append(k)
    x.append(l)

for t in range(i):
    print("Case #{}: {} + {} = {}".format(str(t+1),str(x[2*t]),str(x[2*t+1]),str(m[t])))