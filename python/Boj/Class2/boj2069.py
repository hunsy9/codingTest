#최소공배수와 최대공약수

#두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

#먼저 두개의 수 입력받자.
numList = list(map(int, input().split()))
numList.sort()
bigNum = numList[1]
smallNum = numList[0]
#최대공약수는 재귀함수로 구할 수 있다. gcd..

def gcd(bigNum,smallNum): #num1 = 24, num2 = 18로 가정하자.
    if(smallNum==0): #작은 수가 0이되면 멈추자
        print(bigNum) #작은수가 0이 되었을때 큰수가 최대공약수이다
        return bigNum
    return gcd(smallNum , bigNum%smallNum);\

#최소공배수는 구한 최대공약수로 넘버들을 나눠주고 그 나눠진 몫들이랑 gcd를 곱한값이다.
def lcm(bigNum,smallNum, gcd):
    div1=bigNum//gcd
    div2=smallNum//gcd
    print(div1*div2*gcd)
    return

gcdNum = gcd(bigNum,smallNum)
lcm(bigNum,smallNum,gcdNum)



