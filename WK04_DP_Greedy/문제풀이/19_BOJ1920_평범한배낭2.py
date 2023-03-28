import sys
input = sys.stdin.readline

n, m = map(int, input().split())
total_backpack = [list(map(int,input().split())) for _ in range(n)]
backpack = []
for weight, value, count in total_backpack:
    for _ in range(count):
        backpack.append([weight, value])

dp = [0 for _ in range(m + 1)]

for weight, value in backpack:
    for i in range(len(dp)-1, 0, -1):
        if i - weight >= 0:
            dp[i] = max(dp[i-weight] + value, dp[i])

print(dp[-1])