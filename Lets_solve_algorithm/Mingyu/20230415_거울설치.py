import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    while q:
        cur_row, cur_col, count = q.popleft()
        for i in range(4):
            new_row = cur_row + dr[i]
            new_col = cur_col + dc[i]
            if filed[new_row][new_col] == "#":
                return count
            if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
                continue
            if visited[new_row][new_col]:
                continue
            if filed[new_row][new_col] == ".":
                q.append([new_row, new_col, count])
            if filed[new_row][new_col] == "!":
                q.append([new_row, new_col, count+1])
    return
n = int(input())
filed = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
q = deque([])
end = []
dr = [0,1,0,-1]
dc = [1,0,-1,0]
for i in range(n):
    for j in range(n):
        if filed[i][j] == '#':
            if q:
                end.append(i)
                end.append(j)
                continue
            q.append([i, j, 0])

print(bfs())