def pour(c, w, i, j):
    maxWater = c[j] - w[j]
    MoveWater = min(maxWater, w[i])
    w[i] -= MoveWater
    w[j] += MoveWater
    return w
def search(c, w, states):
    if w not in states:
        states.append(w)
        for i in range(3):
            for j in range(3):
                if i != j: # 모든 경우의 수 i, j
                    new_w = pour(c, w.copy(), i, j)
                    search(c, new_w, states)

C=list(map(int,input().split()))
W=list(map(int,input().split()))
possible = []
search(C, W, possible)
print(len(possible))


