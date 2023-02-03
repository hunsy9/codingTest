MAX=input()
for i in range(int(MAX)):
    sum=int(i)
    for j in str(i):
        sum+=int(j)
    if sum == int(MAX):
        print(i)
        break
    if i == int(MAX)-1:
        print(0)
