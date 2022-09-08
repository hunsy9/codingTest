a=int(input())
b=a-1
for i in reversed(list(range(b))):
    print(" "*(i+1)+"*"*(b-i));
print("*"*a)
for i in range(b):
    print(" "*(i+1)+"*"*(b-i));