a=int(input())
b=[list(input().split(" ")) for i in range(a)]
for i in range(len(b)):
    str=""
    for j in range(len(b[i][1])):
        str+=int(b[i][0])*b[i][1][j]
    print(str)


# T = int(input())
# for t in range(T):
#     N, S = input().split()
#     N = int(N)
#     print(''.join([N*e for e in S]))


