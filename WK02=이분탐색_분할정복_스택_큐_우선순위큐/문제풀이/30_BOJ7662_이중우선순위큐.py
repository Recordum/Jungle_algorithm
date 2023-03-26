import sys
import heapq
input = sys.stdin.readline


result=[]
for test_case in range(int(input())):
    visited = [False] * 1000001
    min_heap = []
    max_heap = []
    for i in range(int(input())):
        instruction = input().split()
        if instruction[0] == 'I':
            heapq.heappush(min_heap, (int(instruction[1]), i))
            heapq.heappush(max_heap, (-1 * int(instruction[1]), i))
            visited[i] = True
            continue
        if instruction[0] == "D" and instruction[1] == '1':
            while True:
                if not max_heap:
                    break
                if max_heap[1]:
                    break
                heapq.heappop(max_heap)
            if max_heap:
                heapq.heappop(max_heap)
                continue
        if instruction[0] == "D" and instruction[1] == '-1':
            while True:
                if not min_heap:
                    break
                if min_heap[1] and not visited[i]:
                    break
                heapq.heappop(min_heap)
            if min_heap:
                heapq.heappop(min_heap)
                visited[i] = True
                continue
    while min_heap :
        heapq.heappop(min_heap)
    while max_heap :
        heapq.heappop(max_heap)
    result.append(f'{-max_heap[0][0]} {min_heap[0][0]}'if max_heap and min_heap else 'EMPTY')
print('\n'.join(result))