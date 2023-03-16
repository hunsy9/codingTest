def isPalindrome(string):
    differCount = 0
    while True:
        if len(string) == 1 or len(string) == 0: #len이 0이거나 1이면 중지
            break
        if string[0] == string[-1]: #맨앞맨끝같으면 그거두개 삭제
            string = string[1:-1]
        else: ##맨앞맨끝 다르면
            print("no")
            return
    if differCount > 1: ## 다 돌았는데 differCount가 2이상일때
        print("no")
        return 3
    print("yes")

while True:
    inp = input()
    if inp == "0":
        break
    isPalindrome(inp)