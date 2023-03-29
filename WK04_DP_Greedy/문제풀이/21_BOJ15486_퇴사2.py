import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
counseling = [list(map(int, input().split())) for _ in range(n)]


for i in range(n)[::-1]:
    time = counseling[i][0]
    value = counseling[i][1]
    if i + time <= n:
        dp[i] = max(dp[i + 1], dp[i+time] + value)
    else:
        dp[i] = dp[i+1]

print(dp[0])