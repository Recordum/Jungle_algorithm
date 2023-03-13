import heapq
import sys
input = sys.stdin.readline

n = int(input())

max_heap = []
min_heap = []
result = []
for _ in range(n):
    number = int(input())
    if not max_heap:
        heapq.heappush(max_heap, -1 * number)
        result.append(-1 * max_heap[0])
        continue

    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -1 *number)
    else:
        heapq.heappush(min_heap, number)

    if -1 * max_heap[0] > min_heap[0]:
        max_value = heapq.heappop(max_heap)
        min_value = heapq.heappop(min_heap)
        heapq.heappush(min_heap, -1 * max_value)
        heapq.heappush(max_heap, -1 * min_value)

    result.append(-1 * max_heap[0])

for ans in result:
    print(ans)
