import sys
import heapq
input = sys.stdin.readline

n = int(input())
card_list = []
count = 0
result = 0
for _ in range(n):
    card = int(input())
    heapq.heappush(card_list, card)

if len(card_list) == 1:
    print(result)
    exit()
for i in range(n-1):
    first = heapq.heappop(card_list)
    second = heapq.heappop(card_list)
    result += first + second
    heapq.heappush(card_list, first+second)

print(result)

