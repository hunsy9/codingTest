N = int(input())
def isParenthesis(inputString):
    stack = []
    count = 0
    for i in range(len(inputString)):
        if inputString[i] == "(":
            stack.append(inputString[i])
        else:
            if len(stack)!=0:
                stack.pop()
            else:
                count += 1
    if len(stack) == 0 and count == 0:
        print("YES")
    else:
        print("NO")

for i in range(N):
    inputString = input().rstrip()
    isParenthesis(inputString)