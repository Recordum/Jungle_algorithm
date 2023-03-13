import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
que = deque([i for i in range(1,n + 1)])
result = []

while que:
    for i in range(k):
        if i == k-1:
            result.append(str(que.popleft()))
            break
        que.append(que.popleft())

print("<"+ ", ".join(result) + ">")