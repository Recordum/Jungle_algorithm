import sys
import heapq

input= sys.stdin.readline
heap = []

n = int(input())
result = []
for _ in range(n):
    number = int(input())
    if number == 0:
        if heap:
            result.append(-1 * heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, -1 * number)

for ans in result:
    print(ans)

