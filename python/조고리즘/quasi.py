def solve(m, n):
    global LCQS, S, T, answer
    for i in range(m, m+2):
        for j in range(n, n+2):
            if i >= len(S) or j >= len(T):
                continue
            elif m == 0 or n == 0:
                if LCQS[i][j] == "":
                    LCQS[i][j] = S[m]
            else:
                if len(LCQS[i][j]) < len(LCQS[m-1][n-1] + S[m]):
                    LCQS[i][j] = LCQS[m-1][n-1] + S[m]
                elif len(LCQS[i][j]) == len(LCQS[m-1][n-1] + S[m]):
                    LCQS[i][j] = min(LCQS[i][j], LCQS[m-1][n-1] + S[m])
            if len(LCQS[i][j]) > len(answer):
                answer = LCQS[i][j]
            elif len(LCQS[i][j]) == len(answer):
                answer = min(answer, LCQS[i][j])


S = input()
T = input()

LCQS = [["" for _ in range(101)] for _ in range(101)]
answer = ""

for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            solve(i, j)

print(answer)

