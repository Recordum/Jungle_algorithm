import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(start):
    visited[start] = True
    for i in range(len(node[start])):
        if not visited[node[start][i]]:
            dfs(node[start][i])
    return True

n, m, = map(int, input().split())
node = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

visited = [False for _ in range(n+1)]
count = 0
for i in range(1, n+1):
    if not visited[i]:
        if dfs(i):
            count += 1
print(count)