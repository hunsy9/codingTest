def isPalindrome(string):
    differCount = 0
    while True:
        if len(string) == 1 or len(string) == 0: #len이 0이거나 1이면 중지
            break
        if string[0] == string[-1]: #맨앞맨끝같으면 그거두개 삭제
            string = string[1:-1]
        else: ##맨앞맨끝 다르면
            differCount += 1 #카운트 하나올리고
            if len(string)!=2 and string[:-1][0] == string[:-1][-1] and string[1:][0] == string[1:][-1]: #만약 맨앞 맨끝
                result1 = isPalindrome(string[1:])
                result2 = isPalindrome(string[:-1])
                if result1 < result2:
                    return result1+1 if result1!=3 else result1
                else:
                    return result2+1 if result2!=3 else result2
            elif string[:-1][0] == string[:-1][-1]:
                string = string[:-1]
            elif string[1:][0] == string[1:][-1]:
                string = string[1:]
            else:
                return 3
    if differCount == 1:
        return 2
    if differCount > 1: ## 다 돌았는데 differCount가 2이상일때
        return 3
    return 1

N = int(input())
for i in range(N):
    print(isPalindrome(input()))
