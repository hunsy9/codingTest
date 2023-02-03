MAX = 100000 #최대
MIN = 10000 #최소

for i in range(MIN, MAX): #10000~100000까지 loop
    tmp = i * 4 #i*4를 tmp에 저장
    num = "".join(reversed(str(i))) #i를 거꾸로 뒤집은 list를 join으로 string으로 만들어 num 에 저장
    if str(tmp) == num: #tmp = num이면
        print("Since 4 x {} is {},".format(i, num))
        print("the special number is {}.".format(num))
        break #for문 종료


# for a in range(1,10):
#     for b in range(0,10):
#         for c in range(0,10):
#             for d in range(0,10):
#                 for e in range(0,10):
#                     list = []
#                     list.append(a)
#                     list.append(b)
#                     list.append(c)
#                     list.append(d)
#                     list.append(e)
#                     result=int("".join(map(str,list)))
#                     reversedResult=int("".join(map(str,reversed(list))))
#                     if 4*result==reversedResult:
#                         print("Since 4 x {} is {},".format(result,reversedResult))
#                         print("the special number is {}.".format(reversedResult))
#                         break
# 다른 방식으로 풀어본 코드입니다.



