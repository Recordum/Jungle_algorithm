import sys
input = sys.stdin.readline


def traver_dfs(depth, start_flag, current_city, cost):
    global result

    visited[current_city] = True

    if depth == n:
        if cost_map[current_city][start_flag] == 0:
            return
        cost = cost + cost_map[current_city][start_flag]
        result = min(result, cost)
        return

    for i in range(n):
        if not visited[i] and cost_map[current_city][i] != 0:
            visited[i] = True
            traver_dfs(depth + 1, start_flag, i, cost + cost_map[current_city][i])
            visited[i] = False
    return

result = 1e9
n = int(input())
cost_map = [list(map(int,input().split())) for _ in range(n) ]

for i in range(n):
    visited = [False] * n
    traver_dfs(1,i,i,0)

print(result)