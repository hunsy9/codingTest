import sys
stack = []
def push(X):
    stack.append(X)
def pop():
    if len(stack) == 0:
        print(-1)
        return
    popedNum = stack.pop()
    print(popedNum)
def size():
    print(len(stack))
def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)
def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

def commandController(command):
    if " " in command:
        push(int(command.split()[1]))
    else:
        if command == "pop":
            pop()
        if command == "size":
            size()
        if command == "empty":
            empty()
        if command == "top":
            top()

N = int(input())
for i in range(N):
    commandController(sys.stdin.readline().rstrip())
