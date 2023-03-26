import sys
from collections import deque
input = sys.stdin.readline
def dfs(start) :
    result[0].append(str(start))
    visited[start] = True
    for i in range(len(node[start])):
        if not visited[node[start][i]]:
            visited[node[start][i]] = True
            dfs(node[start][i])
    return
def bfs(start):
    queue = deque([])
    queue.append(start)
    while queue:
        index = queue.popleft()
        visited[index] = True
        result[1].append(str(index))
        for i in range(len(node[index])):
            if not visited[node[index][i]]:
                visited[node[index][i]] = True
                queue.append(node[index][i])
    return
result = [[] for i in range(2)]
n, m, v = map(int, input().split())
node = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
for no in node:
    no.sort()
visited = [False for i in range(n+1)]
dfs(v)
visited = [False for i in range(n+1)]
bfs(v)
for ans in result:
    print(" ".join(ans))
