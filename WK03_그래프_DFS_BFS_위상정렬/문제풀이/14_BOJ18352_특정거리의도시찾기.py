import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    distance = [0 for _ in range(n+1)]
    q = deque([])
    q.append(start)
    visited[start] = True
    while q:
        city = q.popleft()
        for i in range(len(node[city])):
            if not visited[node[city][i]]:
                visited[node[city][i]] = True
                distance[node[city][i]] = distance[city] + 1
                if distance[node[city][i]] == k:
                    result.append(node[city][i])
                q.append(node[city][i])

    return
result = []
n, m, k, x = map(int, input().split())
node = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
    start, end = map(int,input().split())
    node[start].append(end)
bfs(x)
if not result:
    print(-1)
result.sort()
for ans in result:
    print(ans)
