## 떡먹는호랑이

import sys
input = sys.stdin.readline

d, k = map(int, input().split())

dp = [0]*(d + 1)
dp[d] = k
dp[d-1] = k-1
while True:
    for i in range(d, 2, -1):
        dp[i-2] = dp[i] - dp[i-1]
        if dp[i] < dp[i-1] or dp[i-1] < dp[i-2]:
            break
    if dp[1] > 0 and dp[1] < dp[2]:
        break
    dp[d-1] -= 1

print(dp[1])
print(dp[2])
