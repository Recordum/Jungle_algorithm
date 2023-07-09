import sys
input = sys.stdin.readline

c, n = map(int, input().split())
marketing = [list(map(int, input().split())) for _ in range(n)]
dp = [[1e9] * (c+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, c + 1):
        cost, city_num = marketing[i-1]
        dp[i][j] = dp[i-1][j-1]
        count = 0
        while True:
            if city_num * count >= j:
                dp[i][j] = min(dp[i][j], count*cost)
                break
            dp[i][j] = min(dp[i][j], dp[i-1][j- count * city_num] + cost * count)
            count += 1
print(dp[-1][-1])