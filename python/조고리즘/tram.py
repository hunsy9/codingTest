s, d, t, w = map(int, input().split())
n = int(input())

numOfUse = [0] * 366
for i in range(n):
    d_i, r_i = map(int, input().split())
    numOfUse[d_i] = r_i

dp = [0] * 366
dp[1] = min(s * numOfUse[1], d)

for i in range(2, 366):
    if numOfUse[i] == 0:
        dp[i] = dp[i-1]
    else:
        one_ride = dp[i-1] + s * numOfUse[i]
        oneDay = dp[i-1] + d
        threeDay = dp[max(0, i - 3)] + t
        week = dp[max(0, i - 6)] + w

        dp[i] = min(one_ride, oneDay, threeDay, week)

print(dp[365])













