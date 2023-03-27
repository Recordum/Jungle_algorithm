import heapq
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    global result
    q = deque([])
    q.append((0, 0, 1))
    while q:
        count, jump, locate = q.popleft()
        for i in range(3):
            if jump + d_jump[i] <= 0:
                break
            next_locate = locate + jump + d_jump[i]
            if next_locate == n:
                result = min(result, count + 1)
                return
            if next_locate > n:
                continue
            if next_locate in too_small:
                continue
            if jump+d_jump[i] in dp[next_locate]:
                continue
            dp[next_locate].append(jump + d_jump[i])
            q.append((count + 1, jump+d_jump[i], next_locate))
    return

result = 1e9
d_jump = [1, 0, -1]
n, m = map(int, input().split())
dp = [[] for _ in range(n+1)]
too_small = set(int(input()) for _ in range(m))
if 2 in too_small:
    print(-1)
    exit()
bfs()
if result == 1e9:
    print(-1)
    exit()
print(result)