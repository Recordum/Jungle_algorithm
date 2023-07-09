import sys
input = sys.stdin.readline

n = int(input())
card_value = list(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(len(card_value) + 1)]

for i in range(len(card_value)):
    dp[i+1][0] = card_value[i]

for i in range(1,len(card_value) + 1):
    for j in range(1, n+1):
        dp[i][j] = max(dp[i][j-i] + dp[i][i], dp[i-1][j])

print(dp[-1][-1])

