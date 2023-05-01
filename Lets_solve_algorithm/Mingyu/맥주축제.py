import heapq
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

beer_list = [list(map(int, input().split())) for _ in range(k)]
alcohol = sorted(beer_list, key= lambda x : (x[1]))

preference = []
alcohol_min = 0
for i in range(k):
    if len(preference) >= n:
        heapq.heappop(preference)
    heapq.heappush(preference, alcohol[i][0])
    alcohol_min = alcohol[i][1]
    if sum(preference) >= m:
         break

if sum(preference) < m:
    print(-1)
    exit(0)

print(alcohol_min)