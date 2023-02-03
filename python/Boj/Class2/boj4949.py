import sys
stack=[]
a = []
while True:
    b = sys.stdin.readline().rstrip()
    if b==".":
        break
    a.append(b)
for j in range(len(a)):
    for i in a[j]:
        if i=="[" or i=="(":
            stack.append(i)
        if i=="]":
            if len(stack)==0:
                continue
            if stack[-1]=="[":
                stack.pop()
        if i==")":
            if len(stack)==0:
                continue
            if stack[-1]=="(":
                stack.pop()
        if i==".":
            if len(stack) == 0:
                print("yes")
                break
            else:
                print("no")
                break
    stack=[]


