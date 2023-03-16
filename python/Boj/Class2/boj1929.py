#문제 : M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
#입력 : 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
#출력 : 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

#소수란 1과 자기자신만을 인수로 가짐
def isPrime(start):
    flag = False
    for i in range(2,start):
        if start % i == 0:
            flag = True
    return flag

start, end = map(int,input().split(" "))
total = []
primes = []
if isPrime(start):
    total = [False] + [True] * (end - start)
else:
    total = [True] * (end - start + 1)

for i in range(1, end - start):
    if total[i]:
        primes.append(i)
        for j in total:
            if j % i == 0:
                j = False

for i in primes:
    print(i)














