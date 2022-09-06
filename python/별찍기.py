#첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

a=int(input())
for i in range(a):
    for j in range(i+1):
        print("*"*(i+1));