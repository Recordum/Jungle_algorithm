import sys
input = sys.stdin.readline

n, k = map(int, input().split())
backpack = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k+1) for _ in range(n+1)]

for index, [weight, value] in enumerate(backpack):
    dp[index+1][0] = value

for i in range(1, len(backpack)+1):
    for j in range(1, k+1):
        weight, value, = backpack[i-1]
        if weight == j:
            dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1], dp[i][j-weight])
            continue
        if j == 1 and weight > j:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            continue
        if weight > j:
            dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])
            continue

        if weight < j:
            dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1], dp[i-1][j-weight] + value)

print(dp[-1][-1])

# 4 10
# 1 1
# 1 2
# 1 3
# 1 4
