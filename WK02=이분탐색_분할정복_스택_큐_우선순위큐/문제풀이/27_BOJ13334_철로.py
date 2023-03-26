# Hint : 범위에 들어오는 값들을 최소힙으로 관리
import heapq
import sys
input = sys.stdin.readline

n = int(input())
location_list = [sorted(list(map(int, input().split()))) for _ in range(n)]
location_list.sort()
distance = int(input())
result = 0
start_heap = []
count = 0
temp = 1e9
for i in range(n):
    heapq.heappush(start_heap, location_list[i][0])
while len(start_heap)>1:
    while temp == start_heap[0]:
        heapq.heappop(start_heap)
    start = start_heap[0]
    for i in range(n-len(start_heap),n):
        if location_list[i][0] < start:
            continue
        if start <= location_list[i][0] and location_list[i][1] <= start + distance:
            count += 1
        else :
            result = max(result,count)
            count = 0
            temp = heapq.heappop(start_heap)
            break
print(result)







