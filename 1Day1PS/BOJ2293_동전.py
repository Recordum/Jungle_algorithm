import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0 for i in range(k+1)]
dp[0] = 1
coins = [int(input()) for _ in range(n)]

for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]

print(dp[k])