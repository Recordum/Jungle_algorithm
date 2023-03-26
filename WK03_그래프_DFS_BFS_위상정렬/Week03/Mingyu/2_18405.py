import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global result
    start = []
    for i in range(n):
        for j in range(n):
            if field[i][j]:
                start.append([field[i][j], i, j, 0])
                visited[i][j] = True
    start_sort = sorted(start)
    q = deque(start_sort)
    while q:
        virus, row, col, count = q.popleft()
        if count == s:
            result = field[x-1][y-1]
            return
        for i in range(4):
            n_row = row + d_row[i]
            n_col = col + d_col[i]
            if 0 <= n_row < n and 0<= n_col < n:
                if not visited[n_row][n_col]:
                    field[n_row][n_col] = virus
                    visited[n_row][n_col] = True
                    q.append([virus, n_row, n_col, count + 1])
        result = field[x-1][y-1]
    return

result = 0
n, k = map(int, input().split())
d_row = [1, 0, -1 ,0]
d_col = [0, 1, 0, -1]
visited= [[False] * n for _ in range(n)]
field = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
bfs()
print(result)