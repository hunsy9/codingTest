from collections import deque
N = int(input())
dq = deque(list(range(1,N+1)))
flag = False
while True:
    if len(dq) == 1:
        print(dq[0])
        break
    targetCard = dq[0]
    dq.popleft()
    if not flag: ##remove
        flag = not flag
    else: ##move
        dq.append(targetCard)
        flag = not flag


