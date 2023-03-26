import sys
import heapq
input = sys.stdin.readline


k, n = map(int, input().split())
prime_heap = []
prime_list = list(map(int, input().split()))
for prime in prime_list:
    heapq.heappush(prime_heap, prime)
for _ in range(n):
    heap_number = heapq.heappop(prime_heap)
    for prime in prime_list:
        heapq.heappush(prime_heap, prime * heap_number)
        if heap_number % prime == 0:
            break


print(heap_number)