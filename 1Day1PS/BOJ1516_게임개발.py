import sys
input = sys.stdin.readline
from collections import deque
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

def topolgy_sort():
    q = deque([])
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)
            result[i] = cost[i]
    while(q):
        node = q.popleft()
        if not graph[node]:
            continue
        for next_node in graph[node]:
            indegree[next_node] -= 1
            result[next_node] = max(result[next_node], cost[next_node] + result[node])
            if indegree[next_node] == 0:
                q.append(next_node)

    return
n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
cost = [0] * (n+1)
result = [0] * (n+1)
for i in range(1, n+1):
    build_info = list(map(int, input().split()))
    cost[i] = build_info[0]
    indegree_info = build_info[1:-1]
    for indegree_data in indegree_info:
        graph[indegree_data].append(i)
        indegree[i] += 1 
        
topolgy_sort()

for i in range(1, len(result)):
    print(result[i])

