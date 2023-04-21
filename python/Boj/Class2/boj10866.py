import sys
queue = []
def push_front(X):
    queue.insert(0,X)
def push_back(X):
    queue.append(X)
def pop_front():
    if len(queue) == 0:
        print(-1)
        return
    popedNum = queue[0]
    queue.remove(popedNum)
    print(popedNum)
def pop_back():
    if len(queue) == 0:
        print(-1)
        return
    popedNum = queue[-1]
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
        push_front(int(command.split()[1])) if command.split()[0] == "push_front" else push_back(int(command.split()[1]))
    else:
        if command == "pop_front":
            pop_front()
        if command == "pop_back":
            pop_back()
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
    print(queue)