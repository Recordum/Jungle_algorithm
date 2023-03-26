import sys
from collections import deque

input = sys.stdin.readline


def topological_sort():
    q = deque([])
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    while q:
        next_nodes = q.popleft()
        result.append(str(next_nodes))
        for next_node in node[next_nodes]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                q.append(next_node)
    return

n, m, = map(int,input().split())
result = []
node = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    indegree[b] += 1
topological_sort()
print(" ".join(result))