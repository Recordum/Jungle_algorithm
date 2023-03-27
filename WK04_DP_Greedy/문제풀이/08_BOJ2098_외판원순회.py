import sys
input = sys.stdin.readline

def dfs_traval(current, visited):
    start_city = 0
    if visited == (1 << n) -1:
        if not cost_map[current][start_city]:
            return INF
        return cost_map[current][start_city]
    if dp[current][visited] != INF:
        return dp[current][visited]
    for i in range(1,n):
        if not visited&(1<<i) and cost_map[current][i]:
            dp[current][visited] = min(dp[current][visited], dfs_traval(i, visited|(1<<i)) + cost_map[current][i])
    return dp[current][visited]

n = int(input())
INF = int(1e9)
dp = [[INF] * (1 << n) for _ in range(n)]
cost_map = [list(map(int,input().split())) for _ in range(n)]
print(dfs_traval(0,1))
