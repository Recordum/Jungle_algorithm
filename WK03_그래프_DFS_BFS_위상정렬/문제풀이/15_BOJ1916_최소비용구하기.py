import sys
import heapq
input = sys.stdin.readline

def dijkstra(start_city):
    hq = []
    heapq.heappush(hq, [0, start_city])
    cost_map[start_city] = 0
    while hq:
        cost, city = heapq.heappop(hq)
        if cost_map[city] < cost:
            continue
        for i in range(len(node[city])):
            next_city = node[city][i][0]
            cost = node[city][i][1] + cost_map[city]
            if cost_map[next_city] > cost:
                cost_map[next_city] = cost
                heapq.heappush(hq, [cost, next_city])
    return


n = int(input())
m = int(input())
cost_map = [int(1e9) for _ in range(n+1)]
node = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    node[start].append([end, cost])

start_city, end_city = map(int, input().split())
dijkstra(start_city)
print(cost_map[end_city])




# BFS 시간초과
# def bfs(start_city):
#     q = []
#     q.append(start_city)
#
#     while q:
#         city = q.popleft()
#         for i in range(len(node[city])):
#                 if start_city == city:
#                     cost_map[start_city][city] = 0
#                 new_cost = cost_map[start_city][city] + cost_map[city][node[city][i]]
#                 if cost_map[start_city][node[city][i]] >= new_cost:
#                     cost_map[start_city][node[city][i]] = new_cost
#                     q.append(node[city][i])
#     return
