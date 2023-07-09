import sys
from collections import deque
input = sys.stdin.readline

def bfs(q, target):
    while q:
        cur_node, count = q.popleft()
        if cur_node == target:
            return count
        for i in range(n):
            if graph[cur_node][i] == 1 and not visited[i]:
                visited[i] = True
                q.append([i, count + 1])

    return -1


n = int(input())
x, y = map(int,input().split())
m = int(input())
graph = [[0]*n for _ in range(n)]
visited = [False]*n
for _ in range(m):
    parent, child = map(int, input().split())
    graph[parent-1][child-1] = 1
    graph[child-1][parent-1] = 1

q = deque([])
q.append([x-1, 0])
visited[x-1] = True

print(bfs(q, y-1))
