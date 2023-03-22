import sys
import heapq

# input = sys.stdin.readline
#
# def topology_sort(hq):
#     while hq:
#         vertex = -heapq.heappop(hq)
#         vertex_sort.append(vertex)
#         for i in range(n):
#             connect = node[vertex][i]
#             if connect:
#                 indegree[i] -= 1
#                 if not indegree[i]:
#                     heapq.heappush(hq, -i)
#     return
#
# n = int(input())
# node = [list(map(int, input().rstrip())) for _ in range(n)]
# indegree = [0 for _ in range(n)]
# result = [0 for _ in range(n)]
# vertex_sort = []
# hq = []
# for i in range(n):
#     for j in range(n):
#         if node[i][j]:
#             indegree[j] += 1
#
# for i in range(n):
#     if not indegree[i]:
#         priority = sum(map(int, node[i]))
#         heapq.heappush(hq, -i)
# if not hq:
#     print(-1)
#     exit()
# topology_sort(hq)
#
# for index, vertex in enumerate(vertex_sort):
#     result[vertex] = str(index + 1)
# print(" ".join(result))


def topology_sort():
    q = []
    for i in range(1, n + 1):
        if degree[i] == 0:
            # heappush(q, i)
            heapq.heappush(q, -i)
    # N = 1
    N = n
    while q:
        now = -heapq.heappop(q)
        anw[now] = N

        for k in graph[now]:
            degree[k] -= 1
            if degree[k] == 0:
                heapq.heappush(q, -k)
        # N += 1
        N -= 1


n = int(sys.stdin.readline())
anw = [0] * (n + 1)
degree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(1, n + 1):
    tmp = [0] + list(map(int, sys.stdin.readline().rstrip()))
    for i in range(1, n + 1):
        if tmp[i] == 1:
            # graph[_].append(i)
            # degree[i] += 1
            graph[i].append(_)
            degree[_] += 1
topology_sort()
if anw.count(0) > 1:
    print(-1)
else:
    print(*anw[1:])