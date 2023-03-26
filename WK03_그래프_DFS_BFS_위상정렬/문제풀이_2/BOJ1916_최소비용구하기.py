import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):
    hq = []
    heapq.heappush(hq, [0, start])
    while hq:
        distance, city = heapq.heappop(hq)
        if distance_table[city] < distance:
            continue
        for r_distance, next_city in node[city]:
            n_distance = distance_table[city] + r_distance
            if n_distance < distance_table[next_city]:
                distance_table[next_city] = n_distance
                heapq.heappush(hq, [n_distance, next_city])
    return

n = int(input())
m = int(input())

node = [[] for _ in range(n+1)]
distance_table = [1e9] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    node[a].append([c, b])
start, end = map(int,input().split())
distance_table[start] = 0
dijkstra(start)
print(distance_table[end])

