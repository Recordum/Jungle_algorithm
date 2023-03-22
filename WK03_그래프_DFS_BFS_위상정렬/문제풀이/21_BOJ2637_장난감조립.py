import sys
from collections import deque

input = sys.stdin.readline


def is_basic(component):
    return assemble_map[component][component] == 1


def topology_sort(q):
    while q:
        component = q.popleft()
        for current in node[component]:
            next_component = current[0]
            count = current[1]
            if is_basic(component):
                assemble_map[next_component][component] += count
            else:
                for i in range(1, n + 1):
                    if assemble_map[component][i]:
                        assemble_map[next_component][i] += assemble_map[component][i] * count
            indegree_map[next_component] -= 1
            if not indegree_map[next_component]:
                q.append(next_component)
    return

n = int(input())
m = int(input())
assemble_map = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
node = [[] for _ in range(n + 1)]
indegree_map = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    node[b].append([a, cost])
    indegree_map[a] += 1

q = deque([])
for i in range(1, n + 1):
    if not indegree_map[i]:
        q.append(i)
        assemble_map[i][i] = 1
topology_sort(q)
for index, result in enumerate(assemble_map[n]):
    if result:
        print(index, result)