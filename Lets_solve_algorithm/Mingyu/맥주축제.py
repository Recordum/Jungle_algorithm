import heapq
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

beer_list = [list(map(int, input().split())) for _ in range(k)]
alcohol = sorted(beer_list, key= lambda x : (x[1],x[0]))

total = 0
preference = []
alcohol_min = 0
for i in range(k):
    if len(preference) >= n:
        sub = heapq.heappop(preference)
        total -= sub
    heapq.heappush(preference, alcohol[i][0])
    total += alcohol[i][0]
    alcohol_min = alcohol[i][1]
    if total >= m:
         break

if total < m:
    print(-1)
    exit(0)

print(alcohol_min)