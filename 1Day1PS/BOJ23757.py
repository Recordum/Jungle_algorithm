import sys
import heapq
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
gift_box = list(map(int, input().split()))
children = list(map(int, input().split()))

q_gift_box = []
q_children = deque(children)
for gift in gift_box:
    heapq.heappush(q_gift_box, -gift)

while(True):
    if not q_gift_box or not q_children:
        break

    gift = -heapq.heappop(q_gift_box)
    child = q_children.popleft()

    if gift == child:
        continue

    if gift - child > 0:
        gift = gift - child
        heapq.heappush(q_gift_box,-gift)
        continue

    if gift - child < 0:
        print(0)
        exit()
        continue

print(1)






