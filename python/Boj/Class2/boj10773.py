N=int(input())
a=[]
for i in range(N):
    num=int(input())
    if num!=0:
        a.append(num)
    else:
        del a[len(a)-1]
print(sum(a))
