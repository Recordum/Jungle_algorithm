import sys
from functools import cache

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(start, time, value):
    if start == n - 1:
        if time == 1:
            dp[start] = max(dp[start], value)
        return

    if dp[start] >= value:
        return
    if start + time - 1 > n - 1:
        return
    dp[start] = value

    for i in range(start + 1, len(counseling)):
        if i >= start + time:
            next_time = counseling[i][0]
            next_value = counseling[i][1]
            if start + next_time <= n-1:
                dfs(i, next_time, value + next_value)
    return

n = int(input())
counseling = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * n
for i in range(len(counseling)):
    if dp[i] >= counseling[i][1]:
        continue
    dfs(i, counseling[i][0], counseling[i][1])
print(max(dp))
