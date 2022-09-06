# a= str(input())
# def function():
#     if(len(a)%10):
#         return (len(a)%10)+1
#     else:
#         return len(a)%10
# for (i) in range(len(a)):
#     print(a[10*i:10*(i+1)])

n=input()

for i in range(0,len(n),10):
    print(n[i:i+10])

print(list(range(0,21,4)))