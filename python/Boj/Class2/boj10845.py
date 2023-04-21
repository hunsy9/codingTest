import sys
queue = []
def push(X):
    queue.append(X)
def pop():
    if len(queue) == 0:
        print(-1)
        return

    popedNum = queue[0]
    queue.remove(popedNum)
    print(popedNum)
def size():
    print(len(queue))
def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)
def front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])
def back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])
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
        if command == "front":
            front()
        if command == "back":
            back()

N = int(input())
for i in range(N):
    commandController(sys.stdin.readline().rstrip())