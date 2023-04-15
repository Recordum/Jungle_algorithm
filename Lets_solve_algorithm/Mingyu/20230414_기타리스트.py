import sys
input = sys.stdin.readline


n,s,m = map(int, input().split())
volume_list = list(map(int,input().split()))
dp = [[0] * (m+1) for _ in range(n+1)]
result = -1

dp[0][s] = 1
for i in range(n):
    for j in range(m+1):
        if dp[i][j] == 1:
            if j + volume_list[i] <= m:
                dp[i+1][j + volume_list[i]] = 1
            if j - volume_list[i] >= 0:
                dp[i+1][j - volume_list[i]] = 1

for i in range(m+1):
    if dp[-1][i] == 1:
        result = max(result, i)
print(result)

