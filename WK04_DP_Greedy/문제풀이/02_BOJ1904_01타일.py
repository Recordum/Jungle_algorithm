import sys
input = sys.stdin.readline


n = int(input())
dp = [0] * (n+1)
if n <= 3:
    print(n)
    exit()
dp[1] = 1
dp[2] = 2
dp[3] = 3


for i in range(4, n+1):
    dp[i] = (dp[i-1]+dp[i-2]) % 15746

print(dp[n])