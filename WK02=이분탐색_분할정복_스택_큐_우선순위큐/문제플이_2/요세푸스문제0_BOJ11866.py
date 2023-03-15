import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

n_list = [i for i in range(1,n+1)]
n_queue = deque(n_list)
result = []
count = 0
while n_queue:
    for i in range(k):
        if i == k -1:
            result.append(str(n_queue.popleft()))
            break
        n_queue.append(n_queue.popleft())

print('<'+ ", ".join(result) + '>')

