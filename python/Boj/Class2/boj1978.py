#주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

N=int(input())
list=list(map(int,input().split()))
countNotPrimary = 0
for i in list:
    flag = False
    if i == 1:
        countNotPrimary+=1
    else:
        for j in range(2, i):
            print("{}%{}={}".format(i,j,i%j))
            if i % j == 0:
                flag = True
        if flag:
            countNotPrimary+=1
print(len(list)-countNotPrimary)
