#큰수의법칙 실전문제 92쪽

N,M,K = map(int, input().split())
numList = list(map(int, input().split()))

#일단은 생각해보니까 내림차순 정렬된 배열의 0,1번째 인덱스만 이용하네??
numList.sort() #입력받은 숫자들 정렬하기
numList.reverse() #아 오름차순이네 ->담부턴 그냥 정렬후에 바로 인덱스로 이용하자.

bigNum=0 #가장 큰수 0으로 초기화
while True: #M=8 ,K=3 #일단 계속 돌려 언제까지?
    if M>=K: #M이 K보다 크거나 같은 경우
        bigNum += numList[0]*K #K개까지 더할수있으니까 더하고
        bigNum += numList[1] #1번째 인덱스 숫자도 더해줘
        M-=(K+1) #그리고 더한 갯수만큼 빼주자
    else: #M이 K보다 작은 경우
        bigNum+=(M*numList[0]) #남은 M만큼 다 더하고 종료시키자.
        break
print(bigNum)


#[ 위 풀이의 문제점 ]
#짧은 시간안에 직관적으로 푼건 잘한거 같은데 만약 M이 엄청 커진다면? 그만큼 시간복잡도가 증가하겠지.
#나동빈의 코드를 보자
#
# N,M,K = map(int, input().split())
# data = list(map(int, input().split()))
#
# data.sort() #정렬
# first = data[N-1] #가장 큰수
# second = data[N-2]#두번째로 큰수
#
# #가장 큰 수가 더해지는 횟수 계산
# count = int(M/(K+1)) * K
# count += M % (K+1)
#
# result = 0
# result += (count) * first
# result += (m-count)*second
#
# print(result)



