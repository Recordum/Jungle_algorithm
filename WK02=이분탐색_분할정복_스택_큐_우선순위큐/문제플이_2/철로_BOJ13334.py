import sys
import heapq
input = sys.stdin.readline


n = int(input())
input_list = [sorted(list(map(int, input().split()))) for _ in range(n)]
distance = int(input())

point_heap = []
result = 0
point_list = []
for road in input_list:
    start, end = road
    if end - start <= distance:
        point_list.append(road)

point_list.sort(key=lambda x: x[1])

answer = 0
for i in range(len(point_list)):
    if not point_heap:
        heapq.heappush(point_heap, point_list[i])
        continue

    while point_heap[0][0] < point_list[i][1] - distance:
        heapq.heappop(point_heap)
        if not point_heap:
            break

    heapq.heappush(point_heap, point_list[i])
    result = max(result,len(point_heap))

print(result)

