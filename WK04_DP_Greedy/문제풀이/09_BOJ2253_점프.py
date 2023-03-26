import heapq
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    global result
    q = deque([])
    dp = {}
    q.append((1, 1, 2))
    while q:
        count, jump, locate = q.popleft()
        if locate == n:
            result = min(result, count)
            return
        if locate > n:
            continue
        for i in range(3):
            next_locate = locate + jump + d_jump[i]
            if jump + d_jump[i] <= 0:
                continue
            if next_locate > n:
                continue
            if next_locate in too_small:
                continue
            if next_locate in dp:
                if dp[next_locate] == jump + d_jump[i]:
                    continue
            dp[next_locate] = jump + d_jump[i]
            q.append((count + 1, jump+d_jump[i], next_locate))
    return

result = 1e9
d_jump = [1, 0, -1]
n, m = map(int, input().split())
too_small = {}
for _ in range(m):
    too_small[int(input())] = -1
if 2 in too_small:
    print(-1)
    exit()
bfs()
if result == 1e9:
    print(-1)
    exit()
print(result)