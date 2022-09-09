#첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

a=int(input())
b=a-1
for i in reversed(list(range(b))):
    print("*"*(b-i)+" "*(2*(i+1))+"*"*(b-i));
print("*"*2*a)
for i in range(b):
    print("*"*(b-i)+" "*(2*(i+1))+"*"*(b-i));