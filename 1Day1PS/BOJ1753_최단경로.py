import sys
import heapq

input = sys.stdin.readline


def daijkstra(start):
    hq = []
    heapq.heappush(hq, [0, start])
    cost_map[start] = 0

    while hq:
        cost, current_city = heapq.heappop(hq)
        if cost_map[current_city] < cost:
            continue 
        for next_city, next_cost in graph[current_city]:
            total_cost = next_cost + cost
            if cost_map[next_city] >  total_cost:
                cost_map[next_city] = total_cost
                heapq.heappush(hq, [total_cost, next_city])        
    return

v, e = map(int,input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
cost_map = [1e9] * (v+1)
for _ in range(e):
    start_city, next_city, cost = map(int, input().split())
    graph[start_city].append([next_city, cost])
daijkstra(start)
for i in range(1, len(cost_map)):
    if cost_map[i] == 1e9:
        print("INF")
    else:
        print(cost_map[i])
