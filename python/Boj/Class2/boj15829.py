M=1234567891
R=31
sigma=0
a=int(input())
str=input()
for i,j in enumerate(str):
    sigma+=(ord(j)%96)*(R**(i))
print(sigma%M)


